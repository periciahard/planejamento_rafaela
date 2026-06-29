const files=document.getElementById('files');
files.onchange=()=>{
 preview.innerHTML='';
 [...files.files].forEach(f=>{
  const img=document.createElement('img');
  img.src=URL.createObjectURL(f);
  preview.appendChild(img);
 });
}
function gerar(){
saida.textContent=`Planejamento iniciado.

Professora: Rafaela
Turma: 4º Ano D
Fotos: ${files.files.length}

Próximas versões:
✓ IA identifica disciplina
✓ IA lê as páginas
✓ IA gera planejamento
✓ Exporta Word no modelo Céu Azul`;
}
