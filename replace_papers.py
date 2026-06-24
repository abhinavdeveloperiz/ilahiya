import re

with open(r'c:\InspireZest\ilahiya law college\ilahia\templates\iqac.html', 'r', encoding='utf-8') as f:
    content = f.read()

def generate_links(count, color_class):
    links = []
    for i in range(1, count + 1):
        links.append(f'''          <a href="#" target="_blank"
            class="flex items-center justify-between p-4 rounded-2xl bg-slate-900 border border-slate-700 hover:border-{color_class}-500 transition group">
            <span class="text-white font-medium text-sm">Semester {i} Papers</span>
            <i class="fa-solid fa-download text-{color_class}-400 group-hover:-translate-y-1 transition-transform"></i>
          </a>''')
    return '\n'.join(links)

# 1. Replace "Previous Year Question Papers" lists
# Find BA LLB Previous Papers block
block1_start = content.find('<!-- BA LLB -->')
block1_end = content.find('<!-- LLB -->', block1_start)

# We want to replace the space-y-4 inside BA LLB with the grid of 10 links
new_ba_llb_links = f'''<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{generate_links(10, "blue")}
        </div>'''
# Replace <div class="space-y-4"> ... </div> inside BA LLB
ba_llb_content = content[block1_start:block1_end]
ba_llb_content = re.sub(r'<div class="space-y-4">.*?</div>\s+</div>', new_ba_llb_links + '\n\n      </div>', ba_llb_content, flags=re.DOTALL)
content = content[:block1_start] + ba_llb_content + content[block1_end:]

# 2. Replace Unitary LLB Previous Papers block
block2_start = content.find('<!-- LLB -->')
block2_end = content.find('</section>', block2_start)

new_llb_links = f'''<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{generate_links(6, "green")}
        </div>'''
llb_content = content[block2_start:block2_end]
# Rename LL.B to Unitary LL.B
llb_content = llb_content.replace('LL.B\n            </h3>', 'Unitary LL.B\n            </h3>')
llb_content = re.sub(r'<div class="space-y-4">.*?</div>\s+</div>', new_llb_links + '\n\n      </div>', llb_content, flags=re.DOTALL)
content = content[:block2_start] + llb_content + content[block2_end:]

# 3. Replace "Internal Question Papers" lists
internal_start = content.find('Internal\n        <span class="text-purple-400">\n          Question Papers')
if internal_start != -1:
    block3_start = content.find('<!-- BA LLB -->', internal_start)
    block3_end = content.find('<!-- LLB -->', block3_start)

    new_ba_llb_internal = f'''<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{generate_links(10, "purple")}
        </div>'''
    ba_llb_int_content = content[block3_start:block3_end]
    ba_llb_int_content = re.sub(r'<div class="space-y-4">.*?</div>\s+</div>', new_ba_llb_internal + '\n\n      </div>', ba_llb_int_content, flags=re.DOTALL)
    content = content[:block3_start] + ba_llb_int_content + content[block3_end:]

    block4_start = content.find('<!-- LLB -->', block3_end)
    block4_end = content.find('</section>', block4_start)

    new_llb_internal = f'''<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{generate_links(6, "cyan")}
        </div>'''
    llb_int_content = content[block4_start:block4_end]
    llb_int_content = llb_int_content.replace('LL.B\n            </h3>', 'Unitary LL.B\n            </h3>')
    llb_int_content = re.sub(r'<div class="space-y-4">.*?</div>\s+</div>', new_llb_internal + '\n\n      </div>', llb_int_content, flags=re.DOTALL)
    content = content[:block4_start] + llb_int_content + content[block4_end:]

with open(r'c:\InspireZest\ilahiya law college\ilahia\templates\iqac.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done replacing.")
