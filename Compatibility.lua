-- Standalone compatibility bridge; no Shadowed Unit Frames code is bundled.
-- SUF is a required dependency. This file runs before SUF's PLAYER_LOGIN setup.
if WOW_PROJECT_ID ~= WOW_PROJECT_CLASSIC then
    return
end

local suppliedColors = false
if type(_G.DebuffTypeColor) ~= "table" then
    local palette = {}
    local function addColor(kind, red, green, blue)
        palette[kind] = { r = red, g = green, b = blue }
    end

    addColor("none",    0.8, 0.0, 0.0)
    addColor("Magic",   0.2, 0.6, 1.0)
    addColor("Curse",   0.6, 0.0, 1.0)
    addColor("Disease", 0.6, 0.4, 0.0)
    addColor("Poison",  0.0, 0.6, 0.0)
    palette[""] = palette.none

    _G.DebuffTypeColor = palette
    suppliedColors = true
end

SLASH_SUFCLASSICCOMPATIBILITY1 = "/sufcompat"
SlashCmdList.SUFCLASSICCOMPATIBILITY = function()
    local message
    if suppliedColors then
        message = "Legacy aura color fallback is active."
    else
        message = "An aura color table already existed; it was left unchanged."
    end
    print("Shadowed Unit Frames - Classic & HC Patch 1.0.0: " .. message)
end
