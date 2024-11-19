
```.wezterm.lua
local wezterm = require 'wezterm'

local config = {}

  

-- Function to convert 16-bit values to 8-bit hex format and ensure they are valid hex strings

local function convert_color(red, green, blue)

local r = math.min(math.floor(red / 256), 255) -- Cap at 255

local g = math.min(math.floor(green / 256), 255) -- Cap at 255

local b = math.min(math.floor(blue / 256), 255) -- Cap at 255

return string.format("#%02X%02X%02X", r, g, b)

end

  

-- Convert your provided color values

local background = convert_color(771, 3341, 6168) -- back_red, back_green, back_blue

local cursor = convert_color(0, 25792, 40092) -- cursor_red, cursor_green, cursor_blue

local text = convert_color(61937, 1542, 58339) -- text_red, text_green, text_blue

  

-- Convert the palette array (split into ansi and brights)

local ansi_colors = {

convert_color(25186, 25186, 25186), -- color 1

convert_color(65792, 33667, 29555), -- color 2

convert_color(46260, 64507, 29555), -- color 3

convert_color(2313, 46260, 48573), -- color 4

convert_color(65278, 54227, 0), -- color 5

convert_color(65792, 37008, 65278), -- color 6

convert_color(53713, 53970, 65535), -- color 7

convert_color(62194, 62194, 62194), -- color 8

}

  

local bright_colors = {

convert_color(36751, 36751, 36751), -- color 9

convert_color(65792, 50372, 48830), -- color 10

convert_color(55255, 65021, 47802), -- color 11

convert_color(65535, 65278, 54998), -- color 12

convert_color(63993, 10280, 33667), -- color 13

convert_color(65792, 45746, 65535), -- color 14

convert_color(59110, 59367, 65535), -- color 15

convert_color(65792, 65792, 65792), -- color 16

}

  

-- Define and apply the custom color scheme

config.color_schemes = {

["Laser"] = {

foreground = text, -- Text color

background = background, -- Background color

cursor_bg = cursor, -- Cursor color

cursor_border = cursor, -- Cursor border color

cursor_fg = background, -- Cursor text color

selection_bg = "#4D4D4D", -- Selection background

selection_fg = "#FFFFFF", -- Selection foreground

  

ansi = ansi_colors, -- Standard ANSI colors

brights = bright_colors, -- Bright ANSI colors

},

}

  
  
  

-- Other configurations

-- config.color_scheme = "Laser"

-- config.color_scheme = "Synthwave"

-- config.color_scheme = "AlienBlood"

-- config.color_scheme = "Aardvark Blue"

config.color_scheme = "Cyberdyne"

config.font_size = 17

config.initial_rows = 200

config.initial_cols = 300

config.default_cursor_style = "BlinkingBlock"

config.scrollback_lines = 10000

  

-- Function to toggle transparency

function toggle_transparency(window, pane)

local overrides = window:get_config_overrides() or {}

if not overrides.window_background_opacity then

overrides.window_background_opacity = 0.7

else

overrides.window_background_opacity = nil

end

window:set_config_overrides(overrides)

end

  

-- Keybindings

config.keys = {

{key="Backspace", mods="CMD", action=wezterm.action{SendString="\x15"}}, -- Cmd+Backspace to delete a line

{key="u", mods="CMD", action=wezterm.action_callback(toggle_transparency)}, -- Cmd+U to toggle transparency

{key="LeftArrow", mods="OPT", action=wezterm.action{SendKey={key="Home"}}}, -- Option+Left Arrow to go to the start of the line

{key="RightArrow", mods="OPT", action=wezterm.action{SendKey={key="End"}}}, -- Option+Right Arrow to go to the end of the line

}

  

-- Set the working directory and other options

config.default_cwd = "/Users/devin/repos/projects"

config.window_close_confirmation = "NeverPrompt"

  

-- Mouse binding to copy on selection

config.mouse_bindings = {

{

event = { Up = { streak = 1, button = 'Left' } },

mods = 'NONE',

action = wezterm.action.CompleteSelection 'Clipboard',

},

}

  

return config
```
