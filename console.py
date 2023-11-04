from direct.showbase import DirectObject
from direct.gui.DirectGui import DirectFrame
from direct.task import Task
import text, settings, commands
import inspect

class Console(DirectObject.DirectObject):
    def __init__(self):
        base.taskMgr.doMethodLater(0.8, self.update_text, "UpdateConsoleTask")
        base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
        self.frame = DirectFrame(frameColor=(0, 0, 0, 0.75),
                      frameSize=(-1.5, 1.5, -0.8, 0.8),
                      pos=(0, 0, 1))
        self.frame.hide()
        self.input_text = text.Text(align='left', wordwrap=35)
        self.input_text.text.reparent_to(self.frame)
        self.input_text.new_pos(-1.2, 0.05)
        
        self.input_string = '_'
        self.input_text.new_text(self.input_string)

        self.log = ''
        self.log_y = 1
        self.log_text = text.Text(align='left', wordwrap=30)
        self.log_text.text.reparent_to(self.frame)
        self.log_text.new_pos(-1.2,self.log_y)
        self.log_text.new_colour((0.8,0.8,0.8,1))
        self.prev_string = ''

    def special_strokes(self):
        self.accept('enter', self.run_func)
        self.accept('backspace', self.remove_last)
        self.accept('escape', self.open_console)
        self.accept('arrow_up', self.prev_command)

    def open_console(self):
        if settings.console_open:
            self.ignoreAll()
            settings.free_mouse = False
        else:
            self.accept('keystroke', self.type)
            self.special_strokes()
            settings.free_mouse = True
            
            
        settings.console_open = not settings.console_open
        settings.ui_open = settings.console_open
        self.show_console()

    def prev_command(self):
        if len(self.prev_string) > 1:
            self.input_string = self.prev_string

    def type(self, keyname):
        if len(keyname.encode().decode())>1:
            return
        if not 20<ord(keyname)<126:
            return

        self.input_string = self.input_string[:-1]+keyname+'_'
        self.input_text.new_text(self.input_string)

    def show_console(self):
        if settings.console_open:
            self.frame.show()
        else:
            self.frame.hide()

    def remove_last(self):
        self.input_string = self.input_string[:-2]+'_'
        self.input_text.new_text(self.input_string)

    def update_text(self, task):
        if settings.console_open:
            if self.input_string[-1] == '_':
                self.input_string = self.input_string[:-1] + ' '
                self.input_text.new_text(self.input_string)
            else:
                self.input_string = self.input_string[:-1] + '_'
                self.input_text.new_text(self.input_string)

        return Task.again

    def extract_args(self):
        split = self.input_string.split()
        command = split[0]
        args = []
        if len(split)>1:
            args = split[1:]
        return command, args

    def run_func(self):
        self.prev_string = self.input_string
        self.input_string = self.input_string[:-1]

        try:
            command, args = self.extract_args()
            
            #Fetch command
            if command not in commands.commands_dict:
                output = f"Command '{command}' not found. Type 'help' or '?' for help"
                self.update_log(output)
                return
            else:
                output = commands.commands_dict[command]
            
            #Call command
            parameters = list(inspect.signature(output).parameters)
            if callable(output) and parameters: #Does function expect arguments?
                if parameters == ['args']:
                    output = output(*args)
                elif len(args)==0:
                    output = f"{command} expects arguments {parameters}"
                else:
                    output = output(*args)
            elif callable(output):
                output = output()

        except Exception as e:
            output = f"Oops, I did not like that.\n{e}"

        self.update_log(output)

    def update_log(self, output):
        bottom = abs(self.log_text.text.textNode.getCardTransformed()[2])
        self.log = f'{self.log}\n>{self.input_string}\n\t{output}\n'
        self.log_text.new_text(self.log)
        self.log_y = bottom-0.40
        self.log_text.new_pos(-1.2,self.log_y)
        #The log text will extend up past the screen. However, it shouldn't matter.
        
        self.input_string = '_'
        self.input_text.new_text(self.input_string)

        
    
        





