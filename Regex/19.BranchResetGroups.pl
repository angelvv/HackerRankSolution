S consists of 8 digits.
S must have "---", "-", "." or ":" separator such that string S gets divided in 4 parts, with each part having exactly two digits.
S string must have exactly one kind of separator.
Separators must have integers on both sides.


$Regex_Pattern = '^\d{2}(---|-|.|:)\d{2}\1\d{2}\1\d{2}$';

$Test_String = <STDIN> ;
if($Test_String =~ /$Regex_Pattern/){
    print "true";
} else {
    print "false";
}