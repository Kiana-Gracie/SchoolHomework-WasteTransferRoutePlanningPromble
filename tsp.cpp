#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <math.h>
#include <time.h> 
#include "json.hpp"

using json = nlohmann::json;

const int maxn=110;
const int maxm=210;

struct node{
	int id;
	double w;
	node(int xx=0,double yy=0){
		id=xx; w=yy;
	}
};

struct pos{
	double x,y,w;
	pos (double xx=0,double yy=0,double ww=0){
		x=xx; y=yy; w=ww;
	}
};
double len(pos a,pos b){
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
pos posRand(int down,int right,int weight){
	return pos(rand()%down,rand()%right,(rand()%weight)+1);
}

struct Scheme{
	int n;
	double len;
	std::vector <node> a[maxn];
};

struct Data{
	int m,n;
	pos A,B;
	pos mp[maxm];
};

struct History{
	std::vector <int> id;
	std::vector <double> len; 
};

class InitScheme
{
	public:
		static Scheme run(Data data){
			Scheme item;
			int item_num = 0, t1;
			for (int i=0;i<data.n;i++) item.a[i].clear();
			item.len = 0;
			for (int i=1;i<=data.m;i++){
				t1 = rand()%min((item_num+1),data.n);
				if (t1 == item_num) item_num++;
				item.a[t1].push_back( node(i,data.mp[i].w) );
			}
			for (int i=0;i<item_num;i++){
				item.len += len(data.A,data.mp[item.a[i][0].id]);
				for (int j=1;j<item.a[i].size();j++){
					item.len += len(data.mp[item.a[i][j-1].id],data.mp[item.a[i][j].id]);
				}
				item.len += len(data.mp[item.a[i][item.a[i].size()-1].id],data.B);
			}
			item.n = item_num;
			return item;
		}
	private:
		static int min(int x,int y){
			if (x<y) return x;
			else return y;
		}
};

class Anneal
{
	public:
		Data data;
		json config;
		json logs;
		Scheme BestScheme, NowScheme, NewScheme;
		History his;
		int ThisStep;
		double BestCost, NowCost, NewCost;
		Scheme run(json config, Scheme init, Data data){
			this->data = data;
			this->config = config;
			double InitTemp=1000.0, FinalTemp=0.00001, RateT;
			RateT = exp((log(FinalTemp)-log(InitTemp))/(double)config["StepMax"]);
			BestScheme = init; BestCost = calc(&init);
			NowScheme = init; NowCost = BestCost;
			time_t start=clock();
			double wait_time = config["Refresh"], max_time = config["CalcTime"];
			wait_time = wait_time / 1000.0;
			max_time = max_time - 1;
			time_t last=start,this_time=start;
			ThisStep = 0;
			for (double T=InitTemp;T>=FinalTemp;T=T*RateT){
				ThisStep++;
				if (ThisStep % 10000 == 0){
					his.id.push_back(ThisStep);
					his.len.push_back(BestScheme.len);
				}
				NewScheme = NowScheme;
				changeNewScheme();
				NewCost = calc(&NewScheme);
				if (NewCost <= NowCost || exp((NowCost - NewCost)/T) > randdb() -0.0001 ){
					NowCost = NewCost;
					NowScheme = NewScheme;
				}
				if (NowCost < BestCost){
					BestCost = NowCost;
					BestScheme = NowScheme;
				}
				if (ThisStep % 10 == 0) this_time = clock();
				if ( (this_time - last) / CLOCKS_PER_SEC > wait_time ){
					last = this_time;
					getSimpleLogs();
					std::ofstream out("logs.json");
					if (out)
						out<<logs;
					out.close();
				}
				if ( (this_time - start) / CLOCKS_PER_SEC > max_time ){
					return BestScheme;
				}
			}
			return BestScheme;
		}
		void getSimpleLogs(){
			logs = {};
			logs["TotalLen"] = BestScheme.len;
			logs["StepNum"] = (ThisStep - 10) + rand()%10;
			logs["TruckNumber"] = BestScheme.n;
			logs["PlaceNumber"] = data.m+2;
			logs["Location"][0]["PlaceID"] = 1;
			logs["Location"][0]["X"] = data.A.x;
			logs["Location"][0]["Y"] = data.A.y;
			logs["Location"][1]["PlaceID"] = 2;
			logs["Location"][1]["X"] = data.B.x;
			logs["Location"][1]["Y"] = data.B.y;
			for (int i=1;i<=data.m;i++){
				logs["Location"][i+1]["PlaceID"] = i+2;
				logs["Location"][i+1]["X"] = data.mp[i].x;
				logs["Location"][i+1]["Y"] = data.mp[i].y;
			}
			for (int i=0;i<BestScheme.n;i++){
				logs["Strategy"][i]["TruckID"] = i+1;
				logs["Strategy"][i]["scheme"][0]["X"] = data.A.x;
				logs["Strategy"][i]["scheme"][0]["Y"] = data.A.y;
				for (int j=0;j<BestScheme.a[i].size();j++){
					logs["Strategy"][i]["scheme"][j+1]["X"] = data.mp[BestScheme.a[i][j].id].x;
					logs["Strategy"][i]["scheme"][j+1]["Y"] = data.mp[BestScheme.a[i][j].id].y;
				}
				logs["Strategy"][i]["scheme"][BestScheme.a[i].size()+1]["X"] = data.B.x;
				logs["Strategy"][i]["scheme"][BestScheme.a[i].size()+1]["Y"] = data.B.y;
			}
		}
		void getTotalLogs(){
			getSimpleLogs();
			logs["StepNum"] = (ThisStep/10000)-1;
			logs["AverageLen"] = (double)logs["TotalLen"] / (double)logs["TruckNumber"];
			double max_len = 0;
			for (int i=0;i<BestScheme.n;i++){
				double item_len = 0;
				item_len = len(data.A,data.mp[BestScheme.a[i][0].id]);
				for (int j=1;j<BestScheme.a[i].size();j++){
					item_len += len(data.mp[BestScheme.a[i][j-1].id],data.mp[BestScheme.a[i][j].id]);
				}
				item_len += len(data.mp[BestScheme.a[i][BestScheme.a[i].size()-1].id],data.B);
				if (max_len < item_len) max_len = item_len;
				logs["Strategy"][i]["length"] = item_len;
			}
			logs["LongestLen"] = max_len;
			for (int i=0;i<BestScheme.n;i++){
				logs["Strategy"][i]["scheme"][0]["PlaceID"] = 1;
				logs["Strategy"][i]["scheme"][0]["Load"] = 0;
				for (int j=0;j<BestScheme.a[i].size();j++){
					logs["Strategy"][i]["scheme"][j+1]["PlaceID"] = BestScheme.a[i][j].id+2;
					logs["Strategy"][i]["scheme"][j+1]["Load"] = data.mp[BestScheme.a[i][j].id].w;
				}
				logs["Strategy"][i]["scheme"][BestScheme.a[i].size()+1]["PlaceID"] = 2;
				logs["Strategy"][i]["scheme"][BestScheme.a[i].size()+1]["Load"] = 0;
			}
			for (int i=0;i<(ThisStep)/10000-1;i++){
				logs["log"][i]["Steps"] = his.id[i];
				logs["log"][i]["MinLength"] = his.len[i];
			}
		}
		double calc(Scheme* item){
			item->len = 0;
			for (int i=0;i<item->n;i++){
				item->len += len(data.A,data.mp[item->a[i][0].id]);
				for (int j=1;j<item->a[i].size();j++){
					item->len += len(data.mp[item->a[i][j-1].id],data.mp[item->a[i][j].id]);
				}
				item->len += len(data.mp[item->a[i][item->a[i].size()-1].id],data.B);
			}
			double cost = item->len;
			for (int i=0;i<item->n;i++){
				double load = 0;
				for (int j=0;j<item->a[i].size();j++){
					load += item->a[i][j].w;
				}
				if (load > (double)config["LoadMax"]){
					cost += (load-(double)config["LoadMax"])*1000.0;
				}
			}
			return cost;
		}
		std::vector <int> scheme[maxn];
		double randdb(){
			double t1=rand()%10000,t2=rand()%10000;
			double t3=t1*10000.0+t2;
			return t3/(10000.0*10000.0);
		}
		static int min(int x,int y){
			if (x<y) return x;
			else return y;
		}
		virtual void changeNewScheme(){
			int r1=rand()%NewScheme.n;
			int r2=rand()%NewScheme.a[r1].size();
			int r3=rand()%NewScheme.a[r1].size();
			std::swap(NewScheme.a[r1][r2],NewScheme.a[r1][r3]);
		}
	private:
};

class MutilAnneal: public Anneal{
	public:
		void changeNewScheme(){
			if (ThisStep%2 == 0){
				int r1=rand()%NewScheme.n;
				int r2=rand()%NewScheme.a[r1].size();
				node r3=NewScheme.a[r1][r2];
				NewScheme.a[r1].erase(std::begin(NewScheme.a[r1])+r2);
				// printf("%d",(int)NewScheme.a[r1].size());
				if (NewScheme.a[r1].size() == 0){
					for (int i=r1;i<NewScheme.n-1;i++)
						NewScheme.a[i] = NewScheme.a[i+1];
					NewScheme.a[NewScheme.n-1].clear();
					NewScheme.n--;
				}
				r1=rand()%min((NewScheme.n+1),data.n);
				if (r1==NewScheme.n) NewScheme.n++;
				r2=rand()%(NewScheme.a[r1].size()+1);
				NewScheme.a[r1].insert(std::begin(NewScheme.a[r1])+r2,r3);
			}
			else{
				int r1=rand()%NewScheme.n;
				int r2=rand()%NewScheme.a[r1].size();
				int r3=rand()%NewScheme.a[r1].size();
				std::swap(NewScheme.a[r1][r2],NewScheme.a[r1][r3]);
			}
		}
	private:
};

Data dataRandom(json config){
	if ((config["DataPath"] != NULL)&&(config["DataPath"] != "NULL")){
		std::ifstream in(config["DataPath"]);
		json raw_data={"default"};
		in>>raw_data;
		in.close();
		Data data;
		data.n = raw_data["TrunkMax"];
		data.m = raw_data["GarbageNum"];
		int MaxX = raw_data["MaxX"], MaxY = raw_data["MaxY"], MaxW = raw_data["GarbageMaxWeight"];
		data.A = pos(raw_data["data"][0]["X"], raw_data["data"][0]["Y"], raw_data["data"][0]["W"]);
		data.B = pos(raw_data["data"][1]["X"], raw_data["data"][1]["Y"], raw_data["data"][1]["W"]);
		for (int i=1;i<=data.m;i++){
			data.mp[i] = pos(raw_data["data"][i+1]["X"], raw_data["data"][i+1]["Y"], raw_data["data"][i+1]["W"]);
		}
		return data;
	}
	srand(config["DataSeed"]);
	Data data;
	data.n = config["TrunkMax"];
	data.m = config["GarbageNum"];
	int MaxX = config["MaxX"], MaxY = config["MaxY"], MaxW = config["GarbageMaxWeight"];
	data.A = posRand(MaxX, MaxY, 1);
	data.B = posRand(MaxX, MaxY, 1);
	for (int i=1;i<=data.m;i++){
		data.mp[i] = posRand(MaxX, MaxY, MaxW);
		if (len(data.mp[i],data.A)<10||len(data.mp[i],data.B)<10) i--;
	}
	return data;
}

void solve(json config)
{
	Data data=dataRandom(config);
	srand(config["ModelSeed"]);
	Scheme sch = InitScheme::run(data);
	if (config["Core"] == "annealing"){
		Anneal core;
		sch = core.run(config,sch,data);
		core.getTotalLogs();
		std::ofstream out("logs.json");
		out<<core.logs;
		out.close();
	}
	else{
		MutilAnneal core;
		sch = core.run(config,sch,data);
		core.getTotalLogs();
		std::ofstream out("logs.json");
		out<<core.logs;
		out.close();
	}
}

int main()
{
	
	std::ifstream in("config.json");
	json config={"default"};
	in>>config;
	in.close();
	
	solve(config);
	
	return 0;
}
