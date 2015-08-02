Use the list files in splitup:

1. Put them in /usr/local/GATE_Developer_8.1/plugins/ANNIE/resources/gazetteer

Add a new gazetter (we want case insensitive, so we have to reinitiate it, since it can't be set at runtime):

2. Remove old gazetter (right clip on the gazetter in resources and remove)
3. Right click new > gazetter. Set case sensitive to False
4. Goto Gazetter editor (double click), add e.g.

	filename:weapon_explosives.lst major:weapons minor:explosives
   
   etc. for all of the files.