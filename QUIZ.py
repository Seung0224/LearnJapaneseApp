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

BG       = "#0d0d1a"
CARD_BG  = "#16162a"
BORDER   = "#2e2e50"
ACCENT   = "#7c6af7"
CORRECT  = "#3dd68c"
WRONG    = "#ff5f5f"
TEXT     = "#f0f0ff"
SUBTEXT  = "#6666aa"
DIM      = "#2a2a45"


def rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    canvas.create_arc(x1,     y1,     x1+2*r, y1+2*r, start=90,  extent=90,  style="pieslice", **kwargs)
    canvas.create_arc(x2-2*r, y1,     x2,     y1+2*r, start=0,   extent=90,  style="pieslice", **kwargs)
    canvas.create_arc(x1,     y2-2*r, x1+2*r, y2,     start=180, extent=90,  style="pieslice", **kwargs)
    canvas.create_arc(x2-2*r, y2-2*r, x2,     y2,     start=270, extent=90,  style="pieslice", **kwargs)
    canvas.create_rectangle(x1+r, y1,   x2-r, y2,   **kwargs)
    canvas.create_rectangle(x1,   y1+r, x2,   y2-r, **kwargs)


def make_btn(parent, text, sub, command):
    """시작화면용 큰 선택 버튼"""
    frame = tk.Frame(parent, bg=DIM, cursor="hand2", height=80)
    frame.pack_propagate(False)

    inner = tk.Frame(frame, bg=DIM)
    inner.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(inner, text=text, bg=DIM, fg=TEXT,
             font=("Segoe UI", 17, "bold")).pack()
    tk.Label(inner, text=sub, bg=DIM, fg=SUBTEXT,
             font=("Segoe UI", 11)).pack(pady=(3, 0))

    def on_enter(_):
        frame.config(bg=ACCENT)
        inner.config(bg=ACCENT)
        for w in inner.winfo_children():
            w.config(bg=ACCENT)
    def on_leave(_):
        frame.config(bg=DIM)
        inner.config(bg=DIM)
        for w in inner.winfo_children():
            w.config(bg=DIM)
    def on_click(_):
        command()

    for widget in [frame, inner] + inner.winfo_children():
        widget.bind("<Enter>",    on_enter)
        widget.bind("<Leave>",    on_leave)
        widget.bind("<Button-1>", on_click)

    return frame


class KanaQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("일본어 퀴즈")
        self.geometry("460x560")
        self.resizable(False, False)
        self.configure(bg=BG)

        self.correct      = 0
        self.total        = 0
        self.streak       = 0
        self.kana_list    = []
        self.current_kana   = ""
        self.current_answer = ""
        self.feedback_job   = None
        self.hint_window    = None

        base = os.path.dirname(os.path.abspath(__file__))
        self.table_img_path = os.path.join(base, "Table.png")

        self.start_frame = tk.Frame(self, bg=BG)
        self.quiz_frame  = tk.Frame(self, bg=BG)

        self._build_start()
        self._build_quiz()
        self._show_start()

    # ── 시작 화면 ───────────────────────────────────
    def _build_start(self):
        f = self.start_frame

        tk.Label(f, text="あア", bg=BG, fg=ACCENT,
                 font=("Meiryo", 52, "bold")).pack(pady=(44, 0))

        tk.Label(f, text="일본어 퀴즈", bg=BG, fg=TEXT,
                 font=("Segoe UI", 24, "bold")).pack(pady=(8, 4))

        tk.Label(f, text="모드를 선택하세요", bg=BG, fg=SUBTEXT,
                 font=("Segoe UI", 12)).pack(pady=(0, 28))

        btns = [
            ("히라가나", "あ  い  う  え  お  …", HIRAGANA),
            ("가타카나", "ア  イ  ウ  エ  オ  …", KATAKANA),
            ("전  체",   "히라가나 + 가타카나",    {**HIRAGANA, **KATAKANA}),
        ]
        for label, sub, data in btns:
            btn = make_btn(f, label, sub, lambda d=data: self._start_quiz(d))
            btn.pack(fill="x", padx=48, pady=7)

    def _show_start(self):
        self.quiz_frame.pack_forget()
        self.start_frame.pack(fill="both", expand=True)

    # ── 퀴즈 화면 ───────────────────────────────────
    def _build_quiz(self):
        f = self.quiz_frame

        # 상단 바
        top = tk.Frame(f, bg=BG)
        top.pack(fill="x", padx=24, pady=(20, 0))

        # ← 뒤로가기
        back = tk.Label(top, text="←  메인", bg=BG, fg=SUBTEXT,
                        font=("Segoe UI", 10), cursor="hand2")
        back.pack(side="left")
        back.bind("<Button-1>", lambda e: self._go_back())
        back.bind("<Enter>",    lambda e: back.config(fg=TEXT))
        back.bind("<Leave>",    lambda e: back.config(fg=SUBTEXT))

        # Hint
        self.hint_btn = tk.Label(
            top, text="  Hint  ", bg=DIM, fg=ACCENT,
            font=("Segoe UI", 10, "bold"), cursor="hand2", pady=5
        )
        self.hint_btn.pack(side="left", padx=(10, 0))
        self.hint_btn.bind("<Button-1>", lambda e: self._show_hint())
        self.hint_btn.bind("<Enter>",    lambda e: self.hint_btn.config(bg=ACCENT, fg=TEXT))
        self.hint_btn.bind("<Leave>",    lambda e: self.hint_btn.config(bg=DIM,    fg=ACCENT))

        # 점수
        right = tk.Frame(top, bg=BG)
        right.pack(side="right")

        self.streak_label = tk.Label(right, text="", bg=BG, fg="#f5a623",
                                     font=("Segoe UI", 11))
        self.streak_label.pack(side="left", padx=(0, 12))

        self.score_label = tk.Label(right, text="0 / 0", bg=BG, fg=SUBTEXT,
                                    font=("Segoe UI", 11))
        self.score_label.pack(side="left")

        # 카드
        self.card_canvas = tk.Canvas(f, width=400, height=260,
                                     bg=BG, highlightthickness=0)
        self.card_canvas.pack(pady=(18, 0))

        # 피드백
        self.feedback_label = tk.Label(f, text="", bg=BG, fg=CORRECT,
                                       font=("Segoe UI", 14, "bold"))
        self.feedback_label.pack(pady=(10, 0))

        # 입력창
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

    def _start_quiz(self, data: dict):
        self.kana_list  = list(data.items())
        self.correct    = 0
        self.total      = 0
        self.streak     = 0
        self.score_label.config(text="0 / 0")
        self.streak_label.config(text="")
        self.start_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self._next_question()

    def _go_back(self):
        if self.feedback_job:
            self.after_cancel(self.feedback_job)
            self.feedback_job = None
        self._show_start()

    # ── 퀴즈 로직 ───────────────────────────────────
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

        pct = int(self.correct / self.total * 100)
        self.score_label.config(text=f"{self.correct} / {self.total}  ({pct}%)")
        self.feedback_job = self.after(1000, self._next_question)


if __name__ == "__main__":
    app = KanaQuiz()
    app.mainloop()
