import tkinter as tk
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("カレンダー")

        # 現在の年月
        self.year = datetime.now().year
        self.month = datetime.now().month

        # ヘッダー
        self.header = tk.Label(root, text="", font=("Arial", 16))
        self.header.pack(pady=10)

        # カレンダーのフレーム
        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack()

        # ナビゲーションボタン
        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=5)
        tk.Button(nav_frame, text="<< 前の月", command=self.prev_month).grid(row=0, column=0, padx=5)
        tk.Button(nav_frame, text="次の月 >>", command=self.next_month).grid(row=0, column=1, padx=5)

        # 選択日表示ラベル
        self.selected_label = tk.Label(root, text="日付を選択してください", font=("Arial", 12))
        self.selected_label.pack(pady=5)

        self.show_calendar()

    def show_calendar(self):
        # 既存のカレンダーをクリア
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # ヘッダー更新
        self.header.config(text=f"{self.year}年 {self.month}月")

        # 曜日ラベル
        week_days = ["日", "月", "火", "水", "木", "金", "土"]
        for col, day in enumerate(week_days):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=5).grid(row=0, column=col)

        # カレンダーの日付を配置
        month_calendar = calendar.monthcalendar(self.year, self.month)
        for row, week in enumerate(month_calendar, start=1):
            for col, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text="", borderwidth=1, relief="solid", width=5, height=2).grid(row=row, column=col)
                else:
                    btn = tk.Button(self.calendar_frame, text=str(day), width=5, height=2,
                                    command=lambda d=day: self.select_date(d))
                    btn.grid(row=row, column=col)

    def select_date(self, day):
        self.selected_label.config(text=f"選択した日付: {self.year}年 {self.month}月 {day}日")

    def prev_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.show_calendar()

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.show_calendar()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
