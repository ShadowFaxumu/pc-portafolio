#Paulina Gómez Rodriguez
#El objetivo es que atraves de el estatus de tu perfil de red
#se pueda gestionar, haciendo cambios o simplemente
#pidiendo que se muestren en pantalla

#Se agrego un ErrorAction al 1 y 2 punto


Function showmenu {
    Clear-Host
    Write-Host "Iniciando Menu..."
    Write-Host "1. Ver estatus de perfil"
    Write-Host "2. Cambiar estatus de perfil"
    Write-Host "3. Ver perfil de red actual"
    Write-Host "4. Cambiar perfil de red actual"
    Write-Host "5. Salir"
}
 
showmenu
 
while(($inp = Read-Host -Prompt "Selecciona una opcion") -ne "8"){
 
switch($inp){
        1 {
            Clear-Host
            try {

              Ver-StatusPerfil -ErrorAction Ignore
            } Catch {
                Write-Host -ForegroundColor Blue -BackgroundColor White "Solo se acepta Private o Public"
            }
            pause;
            break 
         }

        2{
            Clear-Host
            try {

              Cambiar-StatusPerfil -ErrorAction Ignore
            } Catch {
                Write-Host -ForegroundColor Blue -BackgroundColor White "Solo se acepta Private o Public"
            }
            pause;
            break  
         }

        3{
            Clear-Host
            Ver-PerfilRedActual
            pause;
            break  
         }

        4{
            Clear-Host
            Cambiar-PerfilRedActual
            pause;
            break
         } 

           
        5 {"Salir"; break}
        default {Write-Host -ForegroundColor red -BackgroundColor white "Opcion invalida. Favor de seleccionar otra opcion";pause}
        
    }

showmenu
}