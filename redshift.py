import bash 
import wx

location=wx.Point(1600, 780)


'''app = wx.App()
frame = wx.Frame(parent=None, title="Redshift")
frame.Show()
app.MainLoop()'''

class MyFrame (wx.Frame):
	def __init__(self):
		super().__init__(parent=None,title="redshift",pos=location,
		size=wx.Size(300,260))
		
		panel = wx.Panel(self)
		my_sizer = wx.BoxSizer(wx.VERTICAL)

		self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
		my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 50)
		self.text_ctrl.Bind(wx.EVT_TEXT_ENTER, self.on_text)

		my_btn = wx.Button(panel,label="DISCHARGE")
		my_btn.Bind(wx.EVT_BUTTON, self.on_press)
		my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
		panel.SetSizer(my_sizer)
		self.Show()

	def on_text(self, event):
		value = self.text_ctrl.GetValue() 
		str = 'exec redshift -O ' + value
		print(str)
		bash.bash(str)	

	def on_press(self, event):
		bash.bash('exec redshift -x')

	

if __name__=="__main__":
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()
