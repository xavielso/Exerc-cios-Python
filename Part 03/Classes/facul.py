"""def funcao(b):
    x=b*b
    return x
x =10
funcao(x)
funcao(x)
print(funcao(x))"""

'''def funcao():
    x = 1
    print(x)
x=10
funcao()
print(x)'''

'''v= [i+10 for i in range(5)]
print(v)'''
<?php
require_once 'usuarios.php';
_______________________
if (isset($_POST['usuario'])){
$user = addslashes($_POST['usuario']);
$passwd = addslashes($_POST['senha']);

if (!empty($usuario) && !empty($senha)){
$u->__________("nomeDB", "localhost", "user", "password");
if ($u->msgErro == ""){
if (!$u->logar($user, $passwd)){
echo "Credenciais incorretas!";
}
} else{
echo "Erro: " . $u->msgErro;
}
} else{
echo "Preencha todos os campos obrigatórios!";

