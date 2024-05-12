import PySimpleGUI as sg
import random

c = ["項目1", "項目2", "項目3", "項目4", "項目5"]

layout = [[sg.I(k="in"), sg.B("OK", k="btn1")],
          [sg.ML("example\nexample\nexample", k="ml"), sg.B("削除", k="del")],
          [sg.FileBrowse("開く", k="btn2", enable_events=True)],
          [sg.T("example", k="txt", enable_events=True)],
          [sg.Combo(c, default_value=c[0], size=(10, 5), k="cb"), sg.B("OK", k="btn3")],
          [sg.Slider(k="sl", range=(40, 208), enable_events=True)],
          [sg.I("40", k="in1", readonly=True)],
          [sg.Listbox(c, size=(10, 5))],
          [sg.Checkbox("項目1", default=True), sg.Checkbox("項目2"), sg.Checkbox("項目3")],
          [sg.Radio("項目1", group_id="rd", k="v1", default=True), sg.Radio("項目2", group_id="rd", k="v2"), sg.Radio("項目3", group_id="rd", k="v3"), sg.B("OK", k="btn4")],
          [sg.B("テーマ一覧", k="btn6")]]
win = sg.Window("example", layout, resizable=True)

r = ["Python", "JavaScript", "Java", "Ruby", "C#", "C言語", "C++"]

while True:
    e, v = win.read()
    win["in1"].update(int(v["sl"]))
    if e == "btn1":
        if v["in"]:
            sg.popup(v["in"]+"が入力されました。", title="example popup")
        else:
            sg.popup_error("入力されていません。", title="example error")
    if e == "btn2":
        sg.popup(v["btn2"]+"/が選択されました。", title=v["btn2"]+"/")
    if e == "txt":
        win["txt"].update(random.choice(r))
    if e == "btn3":
        sg.popup(v["cb"]+"が選択されました。", title="example popup")
    if e == "del":
        p = sg.popup_yes_no("削除してよろしいでしょうか？", title="example popup")
        if p == "Yes":
            win["ml"].update("")
    if e == "btn4":
        if v["v3"] == True:
            sg.popup("正解！", title="example popup")
        else:
            sg.popup("不正解！", title="example popup")
    if e == "btn6":
        sg.theme_previewer()
    if e == None:
        break
win.close()
