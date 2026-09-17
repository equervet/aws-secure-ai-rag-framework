-- Converts a "**PowerShell**" / code block / "**Bash**" / code block sequence
-- into an interactive tabbed widget (see templates/pandoc-template.html for the
-- matching CSS/JS). Plain markdown with these captions still renders cleanly
-- on GitHub without this filter.

local tab_count = 0

local function is_caption(block, text)
  if not block or block.t ~= "Para" then return false end
  local inlines = block.content
  if #inlines ~= 1 or inlines[1].t ~= "Strong" then return false end
  local strong_inlines = inlines[1].content
  return #strong_inlines == 1 and strong_inlines[1].t == "Str" and strong_inlines[1].text == text
end

local function escape_html(s)
  return s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;")
end

function Pandoc(doc)
  local blocks = doc.blocks
  local result = {}
  local i = 1

  while i <= #blocks do
    local ps_caption, ps_code, bash_caption, bash_code =
      blocks[i], blocks[i + 1], blocks[i + 2], blocks[i + 3]

    if is_caption(ps_caption, "PowerShell") and ps_code and ps_code.t == "CodeBlock"
        and is_caption(bash_caption, "Bash") and bash_code and bash_code.t == "CodeBlock" then
      tab_count = tab_count + 1
      local id = "code-tabs-" .. tab_count
      local html = table.concat({
        '<div class="code-tabs">',
        '<input type="radio" class="code-tabs__input code-tabs__input--ps" name="', id, '" id="', id, '-ps" checked>',
        '<label class="code-tabs__label" for="', id, '-ps">PowerShell</label>',
        '<input type="radio" class="code-tabs__input code-tabs__input--bash" name="', id, '" id="', id, '-bash">',
        '<label class="code-tabs__label" for="', id, '-bash">Bash</label>',
        '<div class="code-tabs__panel code-tabs__panel--ps"><pre><code>', escape_html(ps_code.text), '</code></pre></div>',
        '<div class="code-tabs__panel code-tabs__panel--bash"><pre><code>', escape_html(bash_code.text), '</code></pre></div>',
        '</div>',
      })
      table.insert(result, pandoc.RawBlock("html", html))
      i = i + 4
    else
      table.insert(result, blocks[i])
      i = i + 1
    end
  end

  doc.blocks = result
  return doc
end
