import urllib2
import json
import sublime
import sublime_plugin
import subprocess

class JsToCsFromSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                # Grab the JS
                js = self.view.substr(region)
                print js
                cmd = "echo '{0}' | js2coffee".format(js)
                p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                returned_cs = p.stdout.read()
                print returned_cs
                if "SyntaxError" in returned_cs:
                  err = returned_cs.split('\n')
                  sublime.error_message(err[0])
                else:
                  self.view.replace(edit, region, returned_cs)

    def is_enabled(self):
        return True