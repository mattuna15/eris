; *****************************************************************************
; *****************************************************************************
;
;		Name:		fileio.asm
;		Purpose:	File I/O handler
;		Created:	14th March 2020
;		Reviewed: 	TODO
;		Author:		Paul Robson (paul@robsons.org.uk)
;
; *****************************************************************************
; *****************************************************************************


; *****************************************************************************
;
;							Kernel Boot code comes here
;
; *****************************************************************************

.OSXFileOperation
		stm 	r0,#$FFFE
		ret
