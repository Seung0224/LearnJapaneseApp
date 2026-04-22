import random
import tkinter as tk
from PIL import Image, ImageTk
import os

HIRAGANA = {
    "あ": "아",  "い": "이",  "う": "우",  "え": "에",  "お": "오",
    "か": "카", "き": "키", "く": "쿠", "け": "케", "こ": "코",
    "さ": "사", "し": "시", "す": "스", "せ": "세", "そ": "소",
    "た": "타", "ち": "치", "つ": "츠", "て": "테", "と": "토",
    "な": "나", "に": "니", "ぬ": "누", "ね": "네", "の": "노",
    "は": "하", "ひ": "히", "ふ": "후", "へ": "헤", "ほ": "호",
    "ま": "마", "み": "미", "む": "무", "め": "메", "も": "모",
    "や": "야", "ゆ": "유", "よ": "요",
    "ら": "라", "り": "리", "る": "루", "れ": "레", "ろ": "로",
    "わ": "와", "を": "오", "ん": "은",
    "が": "가", "ぎ": "기", "ぐ": "구", "げ": "게", "ご": "고",
    "ざ": "자", "じ": "지", "ず": "즈", "ぜ": "제", "ぞ": "조",
    "だ": "다", "ぢ": "지", "づ": "즈", "で": "데", "ど": "도",
    "ば": "바", "び": "비", "ぶ": "부", "べ": "베", "ぼ": "보",
    "ぱ": "파", "ぴ": "피", "ぷ": "푸", "ぺ": "페", "ぽ": "포",
    "きゃ": "캬", "きゅ": "큐", "きょ": "쿄",
    "しゃ": "샤", "しゅ": "슈", "しょ": "쇼",
    "ちゃ": "챠", "ちゅ": "츄", "ちょ": "쵸",
    "にゃ": "냐", "にゅ": "뉴", "にょ": "뇨",
    "ひゃ": "햐", "ひゅ": "휴", "ひょ": "효",
    "みゃ": "먀", "みゅ": "뮤", "みょ": "묘",
    "りゃ": "랴", "りゅ": "류", "りょ": "료",
    "ぎゃ": "갸", "ぎゅ": "규", "ぎょ": "교",
    "じゃ": "쟈", "じゅ": "쥬", "じょ": "죠",
    "びゃ": "뱌", "びゅ": "뷰", "びょ": "뵤",
    "ぴゃ": "퍄", "ぴゅ": "퓨", "ぴょ": "표",
}

KATAKANA = {
    "ア": "아",  "イ": "이",  "ウ": "우",  "エ": "에",  "オ": "오",
    "カ": "카", "キ": "키", "ク": "쿠", "ケ": "케", "コ": "코",
    "サ": "사", "シ": "시", "ス": "스", "セ": "세", "ソ": "소",
    "タ": "타", "チ": "치", "ツ": "츠", "テ": "테", "ト": "토",
    "ナ": "나", "ニ": "니", "ヌ": "누", "ネ": "네", "ノ": "노",
    "ハ": "하", "ヒ": "히", "フ": "후", "ヘ": "헤", "ホ": "호",
    "マ": "마", "ミ": "미", "ム": "무", "メ": "메", "モ": "모",
    "ヤ": "야", "ユ": "유", "ヨ": "요",
    "ラ": "라", "リ": "리", "ル": "루", "レ": "레", "ロ": "로",
    "ワ": "와", "ヲ": "오", "ン": "은",
    "ガ": "가", "ギ": "기", "グ": "구", "ゲ": "게", "ゴ": "고",
    "ザ": "자", "ジ": "지", "ズ": "즈", "ゼ": "제", "ゾ": "조",
    "ダ": "다", "ヂ": "지", "ヅ": "즈", "デ": "데", "ド": "도",
    "バ": "바", "ビ": "비", "ブ": "부", "ベ": "베", "ボ": "보",
    "パ": "파", "ピ": "피", "プ": "푸", "ペ": "페", "ポ": "포",
    "キャ": "캬", "キュ": "큐", "キョ": "쿄",
    "シャ": "샤", "シュ": "슈", "ショ": "쇼",
    "チャ": "챠", "チュ": "츄", "チョ": "쵸",
    "ニャ": "냐", "ニュ": "뉴", "ニョ": "뇨",
    "ヒャ": "햐", "ヒュ": "휴", "ヒョ": "효",
    "ミャ": "먀", "ミュ": "뮤", "ミョ": "묘",
    "リャ": "랴", "リュ": "류", "リョ": "료",
    "ギャ": "갸", "ギュ": "규", "ギョ": "교",
    "ジャ": "쟈", "ジュ": "쥬", "ジョ": "죠",
    "ビャ": "뱌", "ビュ": "뷰", "ビョ": "뵤",
    "ピャ": "퍄", "ピュ": "퓨", "ピョ": "표",
}

BG         = "#0d0d1a"
CARD_BG    = "#16162a"
BORDER     = "#2e2e50"
ACCENT     = "#7c6af7"
CORRECT    = "#3dd68c"
WRONG      = "#ff5f5f"
TEXT       = "#f0f0ff"
SUBTEXT    = "#6666aa"
DIM        = "#2a2a45"
DIM_GREEN  = "#1a3328"
DIM_PURPLE = "#2a2a45"


def rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    canvas.create_arc(x1,     y1,     x1+2*r, y1+2*r, start=90,  extent=90,  style="pieslice", **kwargs)
    canvas.create_arc(x2-2*r, y1,     x2,     y1+2*r, start=0,   extent=90,  style="pieslice", **kwargs)
    canvas.create_arc(x1,     y2-2*r, x1+2*r, y2,     start=180, extent=90,  style="pieslice", **kwargs)
    canvas.create_arc(x2-2*r, y2-2*r, x2,     y2,     start=270, extent=90,  style="pieslice", **kwargs)
    canvas.create_rectangle(x1+r, y1,   x2-r, y2,   **kwargs)
    canvas.create_rectangle(x1,   y1+r, x2,   y2-r, **kwargs)


def make_btn(parent, text, sub, command, compact=False,
             idle_color=DIM, hover_color=ACCENT):
    h          = 65  if compact else 80
    title_size = 14  if compact else 17
    sub_size   = 9   if compact else 11

    frame = tk.Frame(parent, bg=idle_color, cursor="hand2", height=h)
    frame.pack_propagate(False)

    inner = tk.Frame(frame, bg=idle_color)
    inner.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(inner, text=text, bg=idle_color, fg=TEXT,
             font=("Segoe UI", title_size, "bold")).pack()
    tk.Label(inner, text=sub, bg=idle_color, fg=SUBTEXT,
             font=("Segoe UI", sub_size)).pack(pady=(2, 0))

    def on_enter(_):
        frame.config(bg=hover_color)
        inner.config(bg=hover_color)
        for w in inner.winfo_children():
            w.config(bg=hover_color)
    def on_leave(_):
        frame.config(bg=idle_color)
        inner.config(bg=idle_color)
        for w in inner.winfo_children():
            w.config(bg=idle_color)
    def on_click(_):
        command()

    for widget in [frame, inner] + inner.winfo_children():
        widget.bind("<Enter>",    on_enter)
        widget.bind("<Leave>",    on_leave)
        widget.bind("<Button-1>", on_click)

    return frame


def make_action_btn(parent, text, color, command):
    """완료 화면 하단 액션 버튼"""
    frame = tk.Frame(parent, bg=color, cursor="hand2")
    lbl = tk.Label(frame, text=text, bg=color, fg=TEXT,
                   font=("Segoe UI", 12, "bold"), padx=18, pady=10)
    lbl.pack()

    def on_enter(_):
        frame.config(bg=TEXT); lbl.config(bg=TEXT, fg=color)
    def on_leave(_):
        frame.config(bg=color); lbl.config(bg=color, fg=TEXT)
    def on_click(_):
        command()

    for w in (frame, lbl):
        w.bind("<Enter>",    on_enter)
        w.bind("<Leave>",    on_leave)
        w.bind("<Button-1>", on_click)

    return frame


class KanaQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("일본어 퀴즈")
        self.resizable(False, False)
        self.configure(bg=BG)

        w, h = 540, 620
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x  = (sw - w) // 2
        y  = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

        self.correct        = 0
        self.total          = 0
        self.streak         = 0
        self.kana_list      = []
        self.current_kana   = ""
        self.current_answer = ""
        self.feedback_job   = None
        self.hint_window    = None
        self.no_dupe_mode   = False
        self.deck           = []
        self.deck_total     = 0
        self.wrong_set      = []   # 오답 목록 (중복 없음)

        base = os.path.dirname(os.path.abspath(__file__))
        self.table_img_path = os.path.join(base, "Table.png")

        self.start_frame    = tk.Frame(self, bg=BG)
        self.quiz_frame     = tk.Frame(self, bg=BG)
        self.complete_frame = tk.Frame(self, bg=BG)

        self._build_start()
        self._build_quiz()
        self._build_complete()
        self._show_start()

    # ── 시작 화면 ───────────────────────────────────
    def _build_start(self):
        f = self.start_frame

        tk.Label(f, text="あア", bg=BG, fg=ACCENT,
                 font=("Meiryo", 52, "bold")).pack(pady=(36, 0))
        tk.Label(f, text="일본어 퀴즈", bg=BG, fg=TEXT,
                 font=("Segoe UI", 24, "bold")).pack(pady=(8, 4))
        tk.Label(f, text="모드를 선택하세요", bg=BG, fg=SUBTEXT,
                 font=("Segoe UI", 12)).pack(pady=(0, 14))

        btn_area = tk.Frame(f, bg=BG)
        btn_area.pack(fill="x", padx=20)
        btn_area.columnconfigure(0, weight=1, uniform="col")
        btn_area.columnconfigure(1, weight=1, uniform="col")

        left_col  = tk.Frame(btn_area, bg=BG)
        left_col.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        right_col = tk.Frame(btn_area, bg=BG)
        right_col.grid(row=0, column=1, sticky="nsew", padx=(6, 0))

        tk.Label(left_col,  text="비중복 모드",  bg=BG, fg=CORRECT,
                 font=("Segoe UI", 11, "bold")).pack(pady=(0, 8))
        tk.Label(right_col, text="무한반복 모드", bg=BG, fg=ACCENT,
                 font=("Segoe UI", 11, "bold")).pack(pady=(0, 8))

        btns = [
            ("히라가나", "あ い う え お…", HIRAGANA),
            ("가타카나", "ア イ ウ エ オ…", KATAKANA),
            ("전  체",   "히라가나 + 가타카나",  {**HIRAGANA, **KATAKANA}),
        ]
        for label, sub, data in btns:
            make_btn(left_col,  label, sub,
                     lambda d=data: self._start_quiz(d, no_dupe=True),
                     compact=True,
                     idle_color=DIM_GREEN,  hover_color=CORRECT).pack(fill="x", pady=5)
            make_btn(right_col, label, sub,
                     lambda d=data: self._start_quiz(d, no_dupe=False),
                     compact=True,
                     idle_color=DIM_PURPLE, hover_color=ACCENT).pack(fill="x", pady=5)

    def _show_start(self):
        self.complete_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.start_frame.pack(fill="both", expand=True)

    # ── 퀴즈 화면 ───────────────────────────────────
    def _build_quiz(self):
        f = self.quiz_frame

        top = tk.Frame(f, bg=BG)
        top.pack(fill="x", padx=24, pady=(20, 0))

        back = tk.Label(top, text="←  메인", bg=BG, fg=SUBTEXT,
                        font=("Segoe UI", 10), cursor="hand2")
        back.pack(side="left")
        back.bind("<Button-1>", lambda e: self._go_back())
        back.bind("<Enter>",    lambda e: back.config(fg=TEXT))
        back.bind("<Leave>",    lambda e: back.config(fg=SUBTEXT))

        self.hint_btn = tk.Label(
            top, text="  Hint  ", bg=DIM, fg=ACCENT,
            font=("Segoe UI", 10, "bold"), cursor="hand2", pady=5
        )
        self.hint_btn.pack(side="left", padx=(10, 0))
        self.hint_btn.bind("<Button-1>", lambda e: self._show_hint())
        self.hint_btn.bind("<Enter>",    lambda e: self.hint_btn.config(bg=ACCENT, fg=TEXT))
        self.hint_btn.bind("<Leave>",    lambda e: self.hint_btn.config(bg=DIM,    fg=ACCENT))

        right = tk.Frame(top, bg=BG)
        right.pack(side="right")

        # 비중복 모드 남은 문제 수
        self.remain_label = tk.Label(right, text="", bg=BG, fg=CORRECT,
                                     font=("Segoe UI", 11))
        self.remain_label.pack(side="left", padx=(0, 12))

        self.streak_label = tk.Label(right, text="", bg=BG, fg="#f5a623",
                                     font=("Segoe UI", 11))
        self.streak_label.pack(side="left", padx=(0, 12))

        self.score_label = tk.Label(right, text="0 / 0", bg=BG, fg=SUBTEXT,
                                    font=("Segoe UI", 11))
        self.score_label.pack(side="left")

        self.card_canvas = tk.Canvas(f, width=400, height=260,
                                     bg=BG, highlightthickness=0)
        self.card_canvas.pack(pady=(18, 0))

        self.feedback_label = tk.Label(f, text="", bg=BG, fg=CORRECT,
                                       font=("Segoe UI", 14, "bold"))
        self.feedback_label.pack(pady=(10, 0))

        entry_outer = tk.Frame(f, bg=BORDER, padx=2, pady=2)
        entry_outer.pack(fill="x", padx=40, pady=(8, 4))

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            entry_outer, textvariable=self.entry_var,
            font=("Segoe UI", 22), bg=DIM, fg=TEXT,
            insertbackground=ACCENT, relief="flat", justify="center", bd=0,
        )
        self.entry.pack(fill="x", ipady=13)
        self.entry.bind("<Return>", self._on_submit)
        self.entry.bind("<FocusIn>",  lambda e: entry_outer.config(bg=ACCENT))
        self.entry.bind("<FocusOut>", lambda e: entry_outer.config(bg=BORDER))

        tk.Label(f, text="한글 발음 입력 후  Enter",
                 bg=BG, fg=SUBTEXT, font=("Segoe UI", 9)).pack()

    # ── 완료 화면 ───────────────────────────────────
    def _build_complete(self):
        f = self.complete_frame

        tk.Label(f, text="", bg=BG).pack(pady=(60, 0))

        self.complete_title = tk.Label(f, text="", bg=BG, fg=CORRECT,
                                       font=("Segoe UI", 32, "bold"))
        self.complete_title.pack()

        self.complete_score = tk.Label(f, text="", bg=BG, fg=TEXT,
                                       font=("Segoe UI", 18))
        self.complete_score.pack(pady=(20, 0))

        self.complete_sub = tk.Label(f, text="", bg=BG, fg=SUBTEXT,
                                     font=("Segoe UI", 12))
        self.complete_sub.pack(pady=(8, 0))

        # 버튼 영역 (완료 상태에 따라 동적으로 채움)
        self.complete_btn_area = tk.Frame(f, bg=BG)
        self.complete_btn_area.pack(pady=(40, 0))

    def _show_complete(self):
        if self.feedback_job:
            self.after_cancel(self.feedback_job)
            self.feedback_job = None

        pct      = int(self.correct / self.total * 100) if self.total > 0 else 0
        all_good = len(self.wrong_set) == 0

        # 완료 화면 텍스트 구성
        if all_good:
            self.complete_title.config(text="다 맞추셨습니다!", fg=CORRECT)
            self.complete_sub.config(text="완벽해요! 모든 문제를 정답으로 푸셨습니다.")
        else:
            self.complete_title.config(text="끝났습니다!", fg=ACCENT)
            self.complete_sub.config(text=f"틀린 문제  {len(self.wrong_set)}개")

        self.complete_score.config(
            text=f"정답률  {pct}%  ({self.correct} / {self.total})")

        # 버튼 초기화 후 재구성
        for w in self.complete_btn_area.winfo_children():
            w.destroy()

        if not all_good:
            make_action_btn(
                self.complete_btn_area,
                "틀린 시험 다시보기",
                WRONG,
                self._retry_wrong
            ).pack(side="left", padx=10)

        make_action_btn(
            self.complete_btn_area,
            "홈으로 가기",
            DIM,
            self._show_start
        ).pack(side="left", padx=10)

        # 화면 전환
        self.quiz_frame.pack_forget()
        self.complete_frame.pack(fill="both", expand=True)

    def _retry_wrong(self):
        wrong_data = dict(self.wrong_set)
        self._start_quiz(wrong_data, no_dupe=True)

    # ── 퀴즈 로직 ───────────────────────────────────
    def _start_quiz(self, data: dict, no_dupe: bool = False):
        self.no_dupe_mode = no_dupe
        self.kana_list    = list(data.items())
        self.wrong_set    = []
        self.correct      = 0
        self.total        = 0
        self.streak       = 0

        if no_dupe:
            self.deck       = self.kana_list.copy()
            random.shuffle(self.deck)
            self.deck_total = len(self.deck)
            self.remain_label.config(text=f"남은 문제: {self.deck_total} / {self.deck_total}")
        else:
            self.deck       = []
            self.deck_total = 0
            self.remain_label.config(text="")

        self.score_label.config(text="0 / 0")
        self.streak_label.config(text="")
        self.entry.config(state="normal")
        self.start_frame.pack_forget()
        self.complete_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self._next_question()

    def _go_back(self):
        if self.feedback_job:
            self.after_cancel(self.feedback_job)
            self.feedback_job = None
        self.entry.config(state="normal")
        self._show_start()

    def _draw_card(self, border_color):
        self.card_canvas.delete("all")
        rounded_rect(self.card_canvas, 2, 2, 398, 258, 22,
                     fill=border_color, outline="")
        rounded_rect(self.card_canvas, 5, 5, 395, 255, 20,
                     fill=CARD_BG, outline="")
        self.card_canvas.create_text(
            200, 128, text=self.current_kana,
            font=("Meiryo", 100, "bold"), fill=TEXT, tags="kana"
        )

    def _next_question(self):
        if self.no_dupe_mode:
            if not self.deck:
                self._show_complete()
                return
            self.current_kana, self.current_answer = self.deck.pop(0)
            remaining = len(self.deck)
            self.remain_label.config(text=f"남은 문제: {remaining} / {self.deck_total}")
        else:
            self.current_kana, self.current_answer = random.choice(self.kana_list)

        self.feedback_label.config(text="")
        self._draw_card(BORDER)
        self.entry_var.set("")
        self.entry.focus_set()

    def _show_hint(self):
        if self.hint_window and self.hint_window.winfo_exists():
            self.hint_window.lift()
            return
        win = tk.Toplevel(self)
        win.title("히라가나 · 가타카나 표")
        win.configure(bg=BG)
        win.resizable(False, False)
        self.hint_window = win
        img   = Image.open(self.table_img_path)
        photo = ImageTk.PhotoImage(img)
        lbl   = tk.Label(win, image=photo, bg=BG)
        lbl.image = photo
        lbl.pack(padx=10, pady=10)

    def _on_submit(self, _event=None):
        user = self.entry_var.get().strip()
        if not user:
            return

        self.total += 1
        if self.feedback_job:
            self.after_cancel(self.feedback_job)

        if user == self.current_answer:
            self.correct += 1
            self.streak  += 1
            self.feedback_label.config(
                text=f"정답!    {self.current_kana} = {self.current_answer}", fg=CORRECT)
            self._draw_card(CORRECT)
            self.streak_label.config(text=f"🔥 {self.streak}" if self.streak >= 2 else "")
        else:
            self.streak = 0
            self.feedback_label.config(
                text=f"오답    정답:  {self.current_answer}", fg=WRONG)
            self._draw_card(WRONG)
            self.streak_label.config(text="")
            # 오답 수집 (중복 없이)
            if self.no_dupe_mode:
                pair = (self.current_kana, self.current_answer)
                if pair not in self.wrong_set:
                    self.wrong_set.append(pair)

        pct = int(self.correct / self.total * 100)
        self.score_label.config(text=f"{self.correct} / {self.total}  ({pct}%)")
        self.feedback_job = self.after(1000, self._next_question)


if __name__ == "__main__":
    app = KanaQuiz()
    app.mainloop()
