import wx
import 查询星座
import 星座运势
import 导出运势
import getlength
import getdate
import 类


class Number:
    """接收输入的字符及标记多选选项动作"""
    year = ''
    month = ''
    day = ''
    birthday = -1
    constellation = -1
    fortune = -1


class Data:
    """
    接收转换成 int 型的 Number.year Number.month Number.day
    """
    year = 1
    month = 1
    day = 1


class MyNumberValidator(wx.Validator):
    """建立验证器类"""
    def __init__(self):
        """初始化界面"""
        wx.Validator.__init__(self)
        self.ValidInput = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.StringLength = 0
        self.Bind(wx.EVT_CHAR, self.OnCharChanged)  # 绑定字符改变事件

    def OnCharChanged(self, event):
        """字符改变事件函数 退格键使字符减一 拦截非法输入"""
        # 得到输入字符的 ASCII 码
        keycode = event.GetKeyCode()
        # 退格（ASCII 码 为8），删除一个字符。
        if keycode == 8:
            self.StringLength -= 1
            # 事件继续传递
            event.Skip()
            return

        # 把 ASII 码 转成字符
        InputChar = chr(keycode)

        if InputChar in self.ValidInput:
            # 在允许输入的范围，继续传递该事件。
            event.Skip()
            self.StringLength += 1
            return True
        return False

    def Clone(self):
        """复制一份验证器类并使验证器生效"""
        return MyNumberValidator()

    def Validate(self, win):
        """引用此函数以使用验证器"""
        return True

    def TransferToWindow(self):
        """当与验证器关联的值必须传输到窗口时，调用此可重写函数"""
        return True

    def TransferFromWindow(self):
        """当窗口中的值必须传输到验证器时，调用此可重写函数"""
        return True


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
        """
        初始化界面 定义静态文本、文本输入框、按键及多选选项并绑定事件
            tcl：年份输入框
            tc2：月份输入框
            tc3：日期输入框
            tc4：结果输出框（设为只读）
            cb_birthday：生日多选框
            cb_constellation星座多选框
            cb_fortune：运势多选框
            btn_require：查询按键 按下输出结果
            btn_clear：清除按键 按下清空输入
            btn_close：关闭窗口按键
            btn_export：导出运势按键 按下导出运势到文件

        """
        wx.StaticText(self, -1, '请输入出生年月日', pos=(125, 0), size=(100, -1))
        wx.StaticText(self, -1, '年', pos=(40, 30), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '月', pos=(40, 60), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '日', pos=(40, 90), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '查询结果', pos=(80, 200), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '请选择查询项', pos=(100, 135), size=(100, -1), style=wx.ALIGN_RIGHT)

        self.tc1 = wx.TextCtrl(self, validator=MyNumberValidator(), pos=(145, 20), size=(150, -1),
                               name='TC01', style=wx.TE_CENTER)
        self.tc2 = wx.TextCtrl(self, validator=MyNumberValidator(), pos=(145, 50), size=(150, -1),
                               name='TC02', style=wx.TE_CENTER)
        self.tc3 = wx.TextCtrl(self, validator=MyNumberValidator(), pos=(145, 80), size=(150, -1),
                               name='TC03', style=wx.TE_CENTER)
        self.tc4 = wx.TextCtrl(self, -1, '', pos=(130, 220), size=(160, 160), name='TC04',
                               style=wx.TE_MULTILINE | wx.CB_READONLY)
        self.cb_birthday = wx.CheckBox(self, -1, '生日', pos=(130, 160), name='CB01')
        self.cb_constellation = wx.CheckBox(self, -1, '星座', pos=(190, 160), name='CB02')
        self.cb_fortune = wx.CheckBox(self, -1, '运势', pos=(250, 160), name='CB03')

        btn_require = wx.Button(self, -1, '查询', pos=(300, 220), size=(100, 25))
        btn_clear = wx.Button(self, -1, '清除', pos=(300, 80), size=(100, 25))
        btn_close = wx.Button(self, -1, '关闭窗口', pos=(300, 280), size=(100, 25))
        btn_export = wx.Button(self, -1, '导出运势', pos=(300, 250), size=(100, 25))

        self.tc1.Bind(wx.EVT_TEXT, self.on_year)
        self.tc2.Bind(wx.EVT_TEXT, self.on_month)
        self.tc3.Bind(wx.EVT_TEXT, self.on_day)

        btn_clear.Bind(wx.EVT_BUTTON, self.on_clear, btn_clear)
        btn_require.Bind(wx.EVT_BUTTON, self.on_require, btn_require)
        btn_close.Bind(wx.EVT_BUTTON, self.on_close, btn_close)
        btn_export.Bind(wx.EVT_BUTTON, self.on_export, btn_export)

        self.Bind(wx.EVT_BUTTON, self.on_clear)
        self.Bind(wx.EVT_BUTTON, self.on_require)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(wx.EVT_CLOSE, self.on_export)

        self.cb_birthday.Bind(wx.EVT_CHECKBOX, self.on_birthday)
        self.cb_constellation.Bind(wx.EVT_CHECKBOX, self.on_constellation)
        self.cb_fortune.Bind(wx.EVT_CHECKBOX, self.on_fortune)

    def on_birthday(self, evt):
        """生日选项函数 按下多选项改变生日选项状态"""
        Number.birthday = Number.birthday * -1

    def on_constellation(self, evt):
        """星座选项函数 按下多选项改变星座选项状态"""
        Number.constellation = Number.constellation * -1

    def on_fortune(self, evt):
        """运势选项函数 按下多选项改变运势选项状态"""
        Number.fortune = Number.fortune * -1

    def on_year(self, evt):
        """年函数  获取年份输入框字符串"""
        year = evt.GetString()
        self.tc1.SetValue(year)
        Number.year = year
        Data.year = int(Number.year)

    def on_month(self, evt):
        """月函数 获取月份输入框字符串"""
        month = evt.GetString()
        self.tc2.SetValue(month)
        Number.month = month
        Data.month = int(Number.month)

    def on_day(self, evt):
        """日函数 获取日期输入框字符串"""
        day = evt.GetString()
        self.tc3.SetValue(day)
        Number.day = day
        Data.day = int(Number.day)

    def on_clear(self, evt):
        """清除函数 将年份 月份 日期清空以重新赋值"""
        year = ''
        month = ''
        day = ''
        self.tc1.SetValue(year)
        self.tc2.SetValue(month)
        self.tc3.SetValue(day)
        Number.year = year
        Number.month = month
        Number.month = month
        Data.year = int(Number.year)
        Data.month = int(Number.month)
        Data.day = int(Number.day)

    def on_require(self, evt):
        """查询函数 按多选项勾选情况及年月日输入情况将需要的结果输出"""
        if Number.birthday == 1 and Number.constellation == 1 and Number.fortune == 1:
            if Number.year == '':
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天" + '\r\n' +"星座为：" +
                                   str(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))) +
                                   '\r\n' + "运势为：" +
                                   星座运势.xingzuoyunshi(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
            else:
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天" + '\r\n' +
                                  "离出生到现在有：" + str(getlength.getlength(Data.year, Data.month, Data.day)) + '\r\n'
                                  + "星座为：" + str(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))) +
                                  '\r\n' + "运势为：" +
                                  星座运势.xingzuoyunshi(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
        if Number.birthday == -1 and Number.constellation == 1 and Number.fortune == 1:
            self.tc4.SetValue("星座为：" + str(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))) +
                              '\r\n' + "运势为：" +
                              星座运势.xingzuoyunshi(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
        if Number.birthday == -1 and Number.constellation == -1 and Number.fortune == 1:
            self.tc4.SetValue("运势为：" +
                              星座运势.xingzuoyunshi(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
        if Number.birthday == -1 and Number.constellation == -1 and Number.fortune == -1:
            self.tc4.SetValue("无结果")
        if Number.birthday == -1 and Number.constellation == 1 and Number.fortune == -1:
            self.tc4.SetValue("星座为：" + str(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
        if Number.birthday == 1 and Number.constellation == -1 and Number.fortune == -1:
            if Number.year == '':
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天")
            else:
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天" + '\r\n' +
                                  "离出生到现在有：" + str(getlength.getlength(Data.year, Data.month, Data.day)) + "天")
        if Number.birthday == 1 and Number.constellation == 1 and Number.fortune == -1:
            if Number.year == '':
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天" + '\r\n' +"星座为：" +
                                   str(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
            else:
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天" + '\r\n' +
                                  "离出生到现在有：" + str(getlength.getlength(Data.year, Data.month, Data.day)) + "天" + '\r\n'
                                  + "星座为：" + str(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
        if Number.birthday == 1 and Number.constellation == -1 and Number.fortune == 1:
            if Number.year == '':
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天" + '\r\n' + "运势为：" +
                                   星座运势.xingzuoyunshi(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))
            else:
                self.tc4.SetValue("下一个生日：" + str(getdate.birthgap(Data.month, Data.day)) + "天" + '\r\n' +
                                  "离出生到现在有：" + str(getlength.getlength(Data.year, Data.month, Data.day)) +
                                  "天" + '\r\n' + "运势为：" +
                                  星座运势.xingzuoyunshi(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))

    def on_export(self, evt):
        """导出运势 将运势导出到文件"""

        导出运势.daochuyunshi(星座运势.xingzuoyunshi(查询星座.constellation(类.Birthday(Data.year, Data.month, Data.day))))

    def on_close(self, evt):
        """关闭窗口事件函数 按下关闭窗口关闭窗口"""

        dlg = wx.MessageDialog(None, '确定要关闭本窗口？', '操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Destroy()


if __name__ == '__main__':
    """主函数"""
    import GUI界面
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    print(help(GUI界面))
    app.MainLoop()