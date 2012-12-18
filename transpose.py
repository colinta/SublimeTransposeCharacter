from sublime import Region
from sublime_plugin import TextCommand


class TransposeCharacterCommand(TextCommand):
    def transpose_characters(self, edit, region, reverse):
        if region.a == 0 or region.a == self.view.size():
            return
        # grab the character to the left and right
        l = region.a - 1
        r = region.a
        a = self.view.substr(l)
        b = self.view.substr(r)

        if a == "\n":
            # swap the lines, place the cursor at the end of the current line
            self.view.run_command('swap_line_up')
            return
        elif b == "\n":
            # swap the lines, place the cursor at the end of the current line
            self.view.run_command('swap_line_down')
            return

        # swap a with b and move the cursor to the right, or left if reverse
        dest_region = Region(l, r + 1)
        if reverse:
            sel_region = Region(l, l)
        else:
            sel_region = Region(r + 1, r + 1)

        e = self.view.begin_edit('move_text_horiz')
        self.view.sel().subtract(region)
        self.view.replace(edit, dest_region, b + a)
        self.view.sel().add(sel_region)
        self.view.end_edit(e)

    def transpose_selection(self, edit, region):
        e = self.view.begin_edit('move_text_horiz')
        self.view.sel().subtract(region)
        self.view.sel().add(Region(region.b, region.a))
        self.view.end_edit(e)

    def transpose_regions(self, edit, region_a, region_b):
        selection_a = self.view.substr(region_a)
        selection_b = self.view.substr(region_b)
        self.view.replace(edit, region_a, selection_b)
        self.view.replace(edit, region_b, selection_a)

    def run(self, edit, reverse=False):
        if len(self.view.sel()) == 1:
            region = self.view.sel()[0]
            if region.empty():
                self.transpose_characters(edit, region, reverse)
            else:
                self.transpose_selection(edit, region)

        elif len(self.view.sel()) > 1:
            e = self.view.begin_edit('move_text_horiz')

            regions = [region for region in self.view.sel()]

            if all(region.empty() for region in regions):
                for region in regions:
                    self.transpose_characters(edit, region, reverse)
            else:
                prev_region = None
                for region in regions:
                    if prev_region is not None:
                        self.transpose_regions(edit, region, prev_region)
                        prev_region = None
                    else:
                        prev_region = region

            self.view.end_edit(e)
