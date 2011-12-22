from sublime import Region
from sublime_plugin import TextCommand


class TransposeCharacterCommand(TextCommand):
    def run(self, edit):
        if len(self.view.sel()) == 1:
            region = self.view.sel()[0]
            if region.empty():
                if region.a == 0 or region.a == self.view.size():
                    return
                # grab the character to the left and right
                l = region.a - 1
                r = region.a
                a = self.view.substr(l)
                b = self.view.substr(r)
                if a == "\n":
                    # swap the lines, place the cursor at the end of the current line
                    (row, col) = self.view.rowcol(region.a)
                    l = self.view.line(region.a - 1)
                    r = self.view.line(region.a)
                    a = self.view.substr(l) + "\n"
                    b = self.view.substr(r) + "\n"
                    dest_region = Region(l.a, r.b + 1)
                    sel_region = Region(l.a)
                elif b == "\n":
                    # swap the lines, place the cursor at the end of the current line
                    (row, col) = self.view.rowcol(region.a)
                    l = self.view.line(region.a)
                    r = self.view.line(region.a + 1)
                    a = self.view.substr(l) + "\n"
                    b = self.view.substr(r) + "\n"
                    dest_region = Region(l.a, r.b + 1)
                    sel_region = Region(r.b)
                else:
                    # swap a with b and move the cursor to the right
                    dest_region = Region(l, r + 1)
                    sel_region = Region(r + 1, r + 1)

                e = self.view.begin_edit('move_text_horiz')
                self.view.sel().subtract(region)
                self.view.replace(edit, dest_region, b + a)
                self.view.sel().add(sel_region)
                self.view.end_edit(e)

            else:
                sel_reversed = self.view.substr(region)[::-1]

                e = self.view.begin_edit('move_text_horiz')
                self.view.sel().subtract(region)
                self.view.replace(edit, region, sel_reversed)
                self.view.sel().add(region)
                self.view.end_edit(e)

        else:  # len(self.view.sel()) > 1
            self.view.run_command('transpose')
