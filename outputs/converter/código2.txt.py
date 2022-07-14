def main ( ) : 
	arg1 = int(input()) 
	arg2 = int(input()) 
	arg4 = float(input()) 
	arg5 = float(input()) 
	arg6 = arg1 + arg2 * arg4 
	arg3 = arg2 - arg1 * arg6 
	operacao = arg1 * arg2 / arg3 - arg4 / arg5 * arg6 
	if ( arg6 > arg3 ) : 
		arg5 = arg2 * arg4 
	else : 
		arg1 = arg5 / arg6 
	return arg2 

main()