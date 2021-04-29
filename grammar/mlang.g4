grammar mlang;

number
   : MINUS? DIGIT +
   ;

PLUS
   : '+'
   ;


MINUS
   : '-'
   ;


TIMES
   : '*'
   ;


DIV
   : '/'
   ;


DIGIT
   : ('0' .. '9')
   ;
