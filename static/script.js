function extrairJSON(t){
try{
const a=t.indexOf('{');
const b=t.lastIndexOf('}');
return JSON.parse(t.slice(a,b+1));
}catch(e){return null;}
}

document.getElementById("btnGerar").onclick = async ()=>{

const r = await fetch("https://api.openai.com/v1/responses",{
method:"POST",
headers:{
"Authorization":"Bearer "+document.getElementById("apiKey").value,
"Content-Type":"application/json"
},
body:JSON.stringify({
model:"gpt-4.1-mini",
input:[{role:"user",content:[{type:"input_text",text:"gerar planejamento institucional completo"}]}]
})
});

const j = await r.json();

let text = j.output?.[0]?.content?.map(c=>c.text).join("") || "";

window.data = extrairJSON(text);

document.getElementById("saida").innerText = JSON.stringify(window.data,null,2);
}

document.getElementById("btnWord").onclick = async ()=>{

window.data.semana_inicio = document.getElementById("inicio").value;
window.data.semana_fim = document.getElementById("fim").value;

const form = new FormData();
form.append("planejamento", new Blob([JSON.stringify(window.data)],{type:"application/json"}));

const r = await fetch("/gerar-word",{method:"POST",body:form});

const blob = await r.blob();
const a = document.createElement("a");
a.href = URL.createObjectURL(blob);
a.download="PLANO_V4.docx";
a.click();
}
