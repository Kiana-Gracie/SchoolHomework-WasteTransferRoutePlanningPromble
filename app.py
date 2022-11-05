import main_ui
import config_ui
import analysis_ui
import warning_ui
import answer_ui
import data_ui
import time
import sys
import os
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QMovie
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5


class IOJSON:
    @staticmethod
    def input(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def output(data, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)


class MyFigure(FigureCanvas):
    def __init__(self, width, height, dpi):
        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 创建一个Figure
        super(MyFigure, self).__init__(self.fig)  # 在父类中激活Figure窗口
        self.axes = self.fig.add_subplot(111)  # 调用Figure下面的add_subplot方法


class MyCanvas(MyFigure):
    def clean(self):
        self.axes.clear()

    def create_plot(self, logs, size=1):
        self.axes.scatter(logs["Location"][0]["X"], logs["Location"][0]["Y"], color='red', marker='D', s=50//size)
        self.axes.scatter(logs["Location"][1]["X"], logs["Location"][1]["Y"], color='red', marker='*', s=100//size)
        for i in range(2, logs["PlaceNumber"]):
            self.axes.scatter(logs["Location"][i]["X"], logs["Location"][i]["Y"],
                              color='black', marker='o', s=20//size)

    def create_line(self, logs, who):
        color_list = ['blue', 'green', 'yellow', 'cyan', 'pink', 'purple']
        it_color = -1
        for i in range(logs["TruckNumber"]):
            if who == 0 or who == logs["Strategy"][i]["TruckID"]:
                it_color += 1
                it_x = [j["X"] for j in logs["Strategy"][i]["scheme"]]
                it_y = [j["Y"] for j in logs["Strategy"][i]["scheme"]]
                self.axes.plot(it_x, it_y, markersize=1, linewidth=1, color=color_list[it_color])


class ConfigUi(QtWidgets.QDialog, config_ui.Ui_Dialog):
    def __init__(self, path):
        super(ConfigUi, self).__init__()
        self.setupUi(self)
        self.path = path
        self.on_save_click()
        # 建立按钮联系
        self.save.clicked.connect(self.on_save_click)
        self.return_2.clicked.connect(self.on_return_click)

    def on_return_click(self):
        self.close()

    def on_save_click(self):
        configs = dict()
        if self.radioButton_1.isChecked():
            configs = {
              "Core": "annealing",
              "TrunkMax": 1,
              "LoadMax": 1000000000,
              "GarbageNum": 40,
              "MaxX": 1000,
              "MaxY": 1000,
              "GarbageMaxWeight": 100,
              "CalcTime": 25,
              "DataSeed": 42,
              "ModelSeed": 42,
              "Refresh": 50,
              "StepMax": 10000000
            }
        elif self.radioButton_2.isChecked():
            configs = {
                "Core": "multiannealing",
                "TrunkMax": 6,
                "LoadMax": 1000,
                "GarbageNum": 60,
                "MaxX": 1000,
                "MaxY": 1000,
                "GarbageMaxWeight": 100,
                "CalcTime": 40,
                "DataSeed": 42,
                "ModelSeed": 42,
                "Refresh": 50,
                "StepMax": 5000000
            }
        else:
            if self.checkBox_1.isChecked():
                configs["Core"] = "annealing"
            else:
                configs["Core"] = "multiannealing"
            configs["TrunkMax"] = self.spinBox.value()
            configs["LoadMax"] = self.spinBox_2.value()
            configs["GarbageNum"] = self.spinBox_3.value()
            configs["MaxX"] = self.spinBox_4.value()
            configs["MaxY"] = self.spinBox_5.value()
            configs["GarbageMaxWeight"] = self.spinBox_6.value()
            configs["CalcTime"] = self.spinBox_7.value()
            configs["DataSeed"] = self.spinBox_8.value()
            configs["ModelSeed"] = self.spinBox_9.value()
            configs["Refresh"] = self.spinBox_10.value()
            configs["StepMax"] = self.spinBox_11.value()
        configs["DataPath"] = "NULL"
        IOJSON.output(configs, self.path)


class DataUi(QtWidgets.QDialog, data_ui.Ui_Dialog):
    def __init__(self, path):
        super(DataUi, self).__init__()
        self.setupUi(self)
        self.path = path
        self.on_save_click()
        # 建立按钮联系
        self.pushButton.clicked.connect(self.on_save_click)
        self.pushButton_2.clicked.connect(self.on_return_click)

    def on_return_click(self):
        self.close()

    def on_save_click(self):
        configs = IOJSON.input(self.path)
        if self.radioButton.isChecked():
            configs["DataPath"] = "NULL"
        elif self.radioButton_2.isChecked():
            configs["DataPath"] = str(self.lineEdit.text())
        IOJSON.output(configs, self.path)


class WarningUi(QtWidgets.QDialog, warning_ui.Ui_Dialog):
    def __init__(self):
        super(WarningUi, self).__init__()
        self.setupUi(self)
        # 美化界面
        self.gif = QMovie('warning.gif')
        self.Warning.setMovie(self.gif)
        self.gif.start()


class AcceptUi(QtWidgets.QDialog, answer_ui.Ui_Dialog):
    def __init__(self):
        super(AcceptUi, self).__init__()
        self.setupUi(self)
        # 美化界面
        self.gif = QMovie('accept.gif')
        self.Accept.setMovie(self.gif)
        self.gif.start()


class AnalysisUI(QtWidgets.QDialog, analysis_ui.Ui_Dialog):
    def __init__(self, logs):
        super(AnalysisUI, self).__init__()
        self.setupUi(self)
        # 美化界面
        self.gif = QMovie('吉祥物.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        # 输出折线图
        self.plot_chart = MyFigure(width=3, height=2, dpi=100)
        self.gridlayout1 = QGridLayout(self.PlotFigure)  # 继承容器
        self.gridlayout1.addWidget(self.plot_chart, 0, 1)
        # 输出饼图
        self.pie_chart = MyFigure(width=2, height=2, dpi=100)
        self.gridlayout2 = QGridLayout(self.PieFigure)  # 继承容器
        self.gridlayout2.addWidget(self.pie_chart, 0, 1)
        # 输出路径图
        self.path_chart = MyCanvas(width=1.4, height=1.4, dpi=100)
        self.gridlayout3 = QGridLayout(self.Path)  # 继承容器
        self.gridlayout3.addWidget(self.path_chart, 0, 1)
        self.path_chart.axes.get_xaxis().set_visible(False)
        self.path_chart.axes.get_yaxis().set_visible(False)
        # 建立按钮联系
        self.logs = logs
        self.pushButton.clicked.connect(self.on_button_click)
        self.output_content(logs)

    def on_button_click(self):
        logs = self.logs
        item = self.CarNum.value()
        if 1 <= item <= logs["TruckNumber"]:
            self.lineEdit.setText("{:.1f}".format(logs["Strategy"][item-1]["length"]))
            the_str = ""
            for it in logs["Strategy"][item-1]["scheme"]:
                if it["PlaceID"] == 1:
                    the_str += "从垃圾车集中停放点出发； "
                elif it["PlaceID"] == 2:
                    the_str += "到达垃圾填埋场，卸货；"
                else:
                    the_str += "到达{:d}号垃圾桶，".format(it["PlaceID"]-2)+"装载{:.1f}单位垃圾； ".format(it["Load"])
            self.textEdit.setText(the_str)
            # 画图
            self.path_chart.clean()
            self.path_chart.create_plot(logs, size=5)
            self.path_chart.create_line(logs, who=item)
            self.path_chart.axes.get_xaxis().set_visible(False)
            self.path_chart.axes.get_yaxis().set_visible(False)
            self.path_chart.draw()
            self.path_chart.flush_events()

    def output_content(self, logs):
        x, y = self.get_plot_data(logs)
        self.plot(x, y)
        x, y = self.get_pie_data(logs)
        self.pie(x, y)
        self.TotalLen.setText("{:.1f}".format(self.get_total_len(logs)))
        self.Number.setText("{:d}".format(self.get_number(logs)))
        self.Longest.setText("{:.1f}".format(self.get_longest(logs)))
        self.Average.setText("{:.1f}".format(self.get_average(logs)))

    @staticmethod
    def get_total_len(logs):
        return logs["TotalLen"]

    @staticmethod
    def get_number(logs):
        return logs["TruckNumber"]

    @staticmethod
    def get_longest(logs):
        return logs["LongestLen"]

    @staticmethod
    def get_average(logs):
        return logs["AverageLen"]

    @staticmethod
    def get_plot_data(logs):
        x = [logs["log"][i]["Steps"] for i in range(len(logs["log"]))]
        y = [logs["log"][i]["MinLength"] for i in range(len(logs["log"]))]
        return x, y

    @staticmethod
    def get_pie_data(logs):
        # print("debug: logs['TruckNumber']", logs["TruckNumber"])
        x = [logs["Strategy"][i]["length"] for i in range(logs["TruckNumber"])]
        y = ["{:d}号车".format(logs["Strategy"][i]["TruckID"]) for i in range(logs["TruckNumber"])]
        return x, y

    def plot(self, x, y):
        self.plot_chart.axes.plot(x, y, linewidth=1, markersize=1)

    def pie(self, x, y):
        total = sum(x)
        color_list = ['blue', 'green', 'yellow', 'cyan', 'pink', 'purple']
        colors = []
        for i in range(len(x)):
            colors.append(color_list[i % 6])
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        self.pie_chart.axes.pie(x, labels=y, colors=colors,
                                autopct=lambda pct: "{:.1f}".format(float(pct/100.*total)))


class MainUi(QtWidgets.QDialog, main_ui.Ui_Dialog):
    def __init__(self, log_path, config_path, backstage_path):
        self.flag = 0
        self.log_path = log_path
        self.config_path = config_path
        self.backstage_path = backstage_path
        super(MainUi, self).__init__()
        self.setupUi(self)
        # 输出路径图
        self.chart = MyCanvas(width=1.3, height=1.3, dpi=100)
        self.gridlayout = QGridLayout(self.MainGraph)  # 继承容器
        self.gridlayout.addWidget(self.chart, 0, 1)

        self.ToConfigUI.clicked.connect(self.to_config_ui)
        self.ToAnalysisUI.clicked.connect(self.to_analysis_ui)
        self.ToDataUI.clicked.connect(self.to_data_ui)
        self.BeginMain.clicked.connect(self.begin_main)
        self.OutputAnswer.clicked.connect(self.output_answer)

    def output_answer(self):
        if self.flag == 3:
            logs = IOJSON.input(self.log_path)
            IOJSON.output(logs, "Answer.json")
            page = AcceptUi()
            page.show()
            page.exec()
        else:
            page = WarningUi()
            page.show()
            page.exec()

    def begin_main(self):
        if self.flag != 1 and self.flag != 3:
            page = WarningUi()
            page.show()
            page.exec()
            return
        self.flag = 2

        # 调用后端代码
        firstname = self.backstage_path.split(".")[0]
        os.system("g++ "+self.backstage_path+" -o "+firstname+".exe -std=c++11")
        os.popen(firstname+".exe")
        # print("debug-process 1")

        # 画图
        configs = IOJSON.input(self.config_path)
        max_time = configs["CalcTime"]
        refresh = float(configs["Refresh"])
        start_t = time.time()
        las_step = 0
        while time.time()-start_t <= max_time:
            self.chart.clean()
            try:
                # print("debug-process 2")
                logs = IOJSON.input(self.log_path)  # 读取后端结果
                self.lineEdit.setText("{:.1f}".format(time.time()-start_t))
                las_step = max(las_step, logs["StepNum"])
                self.lineEdit_2.setText("{:d}".format(las_step))
                self.lineEdit_3.setText("{:.1f}".format(logs["TotalLen"]))
                self.chart.create_line(logs, who=0)
                self.chart.create_plot(logs)
                self.chart.draw()
                self.chart.flush_events()
                time.sleep(refresh / 2000)
            except:  # 避免因系统管道读取不全或文件被占用而产生的问题
                pass
        self.flag = 3

    def to_config_ui(self):
        if self.flag != 2:
            page = ConfigUi(self.config_path)
            page.show()
            page.exec()
            if self.flag <= 1:
                self.flag = 1
        else:
            page = WarningUi()
            page.show()
            page.exec()

    def to_data_ui(self):
        page = DataUi(self.config_path)
        page.show()
        page.exec()

    def to_analysis_ui(self):
        if self.flag >= 3:
            # 读取后端结果
            time.sleep(1.0)
            logs = IOJSON.input(self.log_path)
            # 转跳页面
            page = AnalysisUI(logs)
            page.show()
            page.exec()
        else:
            page = WarningUi()
            page.show()
            page.exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    a = MainUi(
        log_path="logs.json",
        config_path="config.json",
        backstage_path="tsp.cpp"
    )
    a.show()

    sys.exit(app.exec_())
