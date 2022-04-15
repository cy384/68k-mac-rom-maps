macintosh ROM maps
==================
This is a quick hack to generate Macintosh ROM map files that can be loaded into Ghidra.  Apple released ROM maps with MPW.  These are pulled from MPW 3.5 "gold master".  I then converted them into unix line endings and munged them into the right format.

Use with Ghidra's "ImportSymbolsScript.py" and a copy of the ROM you want to look at.

Don't see your mac listed?  It's got the same map as one of the other ones.  See "Makefile" to figure out which one, if you don't already know.

notes
-----

ran on bash/linux:

	for FILE in from-mpw-gm-3.5/ROM\ Maps/ROM.List/*.lst ; do tr '\r' '\n' < "$FILE" | tail -n +9 | awk '{print $1, $3, "l"}' | head -n -1 | sed "s/ \$[0-9][0-9]\,/ /" | sed "s/\\$/0x/" | cat > "$FILE.txt" ; mv "$FILE.txt" rom-maps/ ; done

From "ImportSymbolsScript.py" file, which says:

"Imports a file with lines in the form "symbolName 0xADDRESS function_or_label" where "f" indicates a function and "l" a label"

I just add an l to everything because Apple's ROM maps aren't obvious in what is what.

there's a mystery here: in the ROM map files, a line can end with an "E", a "#", or nothing

* E seems to be functions? entry/exit something? public or something?
* # seems to be data?
* nothing who knows?
