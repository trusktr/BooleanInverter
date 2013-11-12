# BooleanInverter

Sublime Text 3 plugin - instantly toggle boolean values in code.

For example you can stand on a line of code which contains the term TRUE and toggle it to FALSE.

	<add key="DefaultEnable" value="TRUE" />

will result with 

	<add key="DefaultEnable" value="FALSE" />

similarly:

	_didLoad = YES;      -> _didLoad = NO;
	m_bEnabled = false;  -> m_bEnabled = true;

## Usage

To toggle term, place the cursor on the desired term or to the left on the same line:

	Super + Alt + I for Mac OS X
	Ctrl + Alt + I for Windows/Linux
