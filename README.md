macintosh ROM maps
==================
This is a quick hack to generate Macintosh ROM map files that can be loaded into Ghidra.  Apple released ROM maps with MPW.  These are pulled from MPW 3.5 "gold master".  I then converted them into unix line endings and munged them into the right format.  The converted maps are in the "rom-maps" folder.

Don't see your mac listed?  It's got the same map as one of the other ones.  See "Makefile" to figure out which one, if you don't already know.

how to use
----------
1. Get Ghidra and make a new project
2. Import the Mac ROM, probably as 68000 binary (or 020, or 040)
3. Open it
4. In the menu, click Window > Script Manager
5. Doubleclick ImportSymbolsScript
6. Select the ROM map
7. Voila

If you want a nice starting point, go to the first label that's something like "INITSTART", click, and hit 'd', which will start some disassembly.

notes
-----

ran on bash/linux:

	for FILE in from-mpw-gm-3.5/ROM\ Maps/ROM.List/*.lst ; do tr '\r' '\n' < "$FILE" | tail -n +9 | awk '{print $1, $3, "l"}' | head -n -1 | sed "s/ \$[0-9][0-9]\,/ /" | sed "s/\\$/0x/" | cat > "$FILE.txt" ; mv "$FILE.txt" rom-maps/ ; done

"ImportSymbolsScript.py" Ghidra file says:

"Imports a file with lines in the form "symbolName 0xADDRESS function_or_label" where "f" indicates a function and "l" a label"

I just add an l to everything because Apple's ROM maps aren't obvious in what is what.

there's a mystery here: in the ROM map files, a line can end with an "E", a "#", or nothing:

* "E" seems to be functions? entry/exit something? public or something?
* "#" seems to be data?
* nothing who knows?

A traps bonus
-------------
Want to be able to diassemble Mac code without Ghidra crying at every A trap?  Paste the contents of "ghidra-a-traps.txt" into "68000.sinc" below the line starting with ":nop".

This basically inserts ~1000 A traps as opcodes without providing any information to Ghidra about what they do.  Still very helpful for manually inspecting code!
