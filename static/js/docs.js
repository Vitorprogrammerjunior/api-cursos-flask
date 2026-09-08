const baseUrlEl = document.getElementById("base-url");
if (baseUrlEl) {
  baseUrlEl.textContent = window.location.origin;
}

function montarCaminho(pathTemplate, paramName, valor) {
  if (!paramName) {
    return pathTemplate;
  }
  return pathTemplate.replace(`{${paramName}}`, encodeURIComponent(valor));
}

function formatarJson(texto) {
  try {
    return JSON.stringify(JSON.parse(texto), null, 2);
  } catch (erro) {
    return texto;
  }
}

document.querySelectorAll("[data-try]").forEach((botao) => {
  botao.addEventListener("click", async () => {
    const secao = botao.closest(".endpoint");
    const resultado = secao.querySelector(".try-result");
    const pathTemplate = secao.dataset.path;
    const paramName = secao.dataset.param;
    const campo = secao.querySelector(`input[name="${paramName}"]`);
    const valor = campo ? campo.value : "";
    const url = montarCaminho(pathTemplate, paramName, valor);

    resultado.hidden = false;
    resultado.innerHTML = "<p>Carregando...</p>";

    try {
      const resposta = await fetch(url);
      const corpo = await resposta.text();
      const classe = resposta.ok ? "ok" : "err";
      resultado.innerHTML = `
        <div class="status-line">
          <span class="pill ${classe}">${resposta.status} ${resposta.statusText}</span>
          <code>${url}</code>
        </div>
        <pre class="example"><code>${formatarJson(corpo)}</code></pre>
      `;
    } catch (erro) {
      resultado.innerHTML = `
        <div class="status-line">
          <span class="pill err">falha de rede</span>
        </div>
        <pre class="example"><code>${erro.message}</code></pre>
      `;
    }
  });
});
