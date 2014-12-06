from subprocess import Popen
import time, pythoncom

    

if __name__ == "__main__":
    print "WSR Speech Recognition is garbage; it is recommended that you not run Sorcery this way."
    import __init__
    import _main
    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(.1)
else:
    
    from dragonfly import Choice, MappingRule, Grammar, Function
    import natlink
    from lib import paths, utilities
    
    def deactivate_natlink():
        natlink.setMicState("sleeping")
        
    def activate_wsr():
        Popen([paths.WSR_PATH, "-SpeechUX"],shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)
    
    def kill_wsr():
        utilities.kill_process("sapisvr.exe")
        
    class WSR_Rule(MappingRule):
    
        
        mapping = {
            "start listening":                      Function(deactivate_natlink),
            "(W S R | W S are)":                    Function(activate_wsr),
            "kill speech":                          Function(kill_wsr)
        
        }
        extras = []
        defaults = {}

                
                    
            
    wsra_rule = WSR_Rule()
    grammar = Grammar('wsr hijack rule')
    grammar.add_rule(wsra_rule)
    grammar.load()