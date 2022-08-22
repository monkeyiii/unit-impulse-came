
import wx


class MainFrame(wx.Frame):
    """从wx.Frame派生主窗口类"""

    def __init__(self, parent):
        """构造函数"""

        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE)

        self.SetTitle('星座运势查询小程序')
        # self.SetIcon(wx.Icon('res/wx.ico'))
        self.SetBackgroundColour((224, 224, 224))  # 设置窗口背景色
        self.SetSize((450, 450))
        self._init_ui()
        self.Center()

    def _init_ui(self):
        """初始化界面"""
        wx.StaticText(self, -1, '请输入出生年月日', pos=(125, 0), size=(100, -1))
        wx.StaticText(self, -1, '年', pos=(40, 30), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '月', pos=(40, 60), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '日', pos=(40, 90), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '查询结果', pos=(80, 200), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '请选择查询项', pos=(100, 135), size=(100, -1), style=wx.ALIGN_RIGHT)

        self.tc1 = wx.TextCtrl(self, -1, '', pos=(145, 20), size=(150, -1), name='TC01', style=wx.TE_CENTER)
        self.tc2 = wx.TextCtrl(self, -1, '', pos=(145, 50), size=(150, -1), name='TC02', style=wx.TE_CENTER)
        self.tc3 = wx.TextCtrl(self, -1, '', pos=(145, 80), size=(150, -1), name='TC03', style=wx.TE_CENTER)
        self.tc4 = wx.TextCtrl(self, -1, '', pos=(130, 220), size=(160, 80), name='TC04',
                               style=wx.TE_MULTILINE | wx.CB_READONLY)
        self.cb_birthday = wx.CheckBox(self, -1, '生日', pos=(130, 160), name='CB01')
        self.cb_constellation = wx.CheckBox(self, -1, '星座', pos=(190, 160), name='CB02')
        self.cb_fortune = wx.CheckBox(self, -1, '运势', pos=(250, 160), name='CB03')

        btn_require = wx.Button(self, -1, '查询', pos=(300, 220), size=(100, 25))
        btn_clear = wx.Button(self, -1, '清除', pos=(300, 80), size=(100, 25))
        btn_close = wx.Button(self, -1, '关闭窗口', pos=(300, 270), size=(100, 25))

        self.tc1.Bind(wx.EVT_TEXT, self.on_year)
        self.tc2.Bind(wx.EVT_TEXT, self.on_month)
        self.tc3.Bind(wx.EVT_TEXT, self.on_day)
        self.tc3.Bind(wx.EVT_TEXT, self.on_result)

        btn_clear.Bind(wx.EVT_BUTTON, self.on_clear, btn_clear)
        btn_require.Bind(wx.EVT_BUTTON, self.on_require, btn_require)
        btn_close.Bind(wx.EVT_BUTTON, self.on_close, btn_close)

        self.Bind(wx.EVT_BUTTON, self.on_clear)
        self.Bind(wx.EVT_BUTTON, self.on_require)
        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.Bind(wx.EVT_CHECKBOX, self.on_birthday)
        self.Bind(wx.EVT_CHECKBOX, self.on_constellation)
        self.Bind(wx.EVT_CHECKBOX, self.on_fortune)

    def on_birthday(self, evt):
        """生日选项函数"""

    def on_constellation(self, evt):
        """星座选项函数"""

    def on_fortune(self, evt):
        """运势选项函数"""

    def on_year(self, evt):
        """年函数"""
        year = evt.GetInt()
        self.tc1.SetValue(year)

    def on_month(self, evt):
        """月函数"""
        month = evt.GetInt
        self.tc2.SetValue(month)

    def on_day(self, evt):
        """日函数"""
        day = evt.GetInt
        self.tc3.SetValue(day)

    def on_result(self, evt):
        """结果函数"""

    def on_clear(self, evt):
        """清除函数"""
        self.tc1.SetValue('')
        self.tc2.SetValue('')
        self.tc3.SetValue('')

    def on_require(self, evt):
        """查询函数"""

    def on_close(self, evt):
        """关闭窗口事件函数"""

        dlg = wx.MessageDialog(None, '确定要关闭本窗口？', '操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()