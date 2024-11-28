// Função para buscar o IP público usando o serviço ipify
async function fetchIP() {
    try {
      const response = await fetch("https://api.ipify.org?format=json");
      const data = await response.json();
  
      // Criar o elemento do pop-up
      const popup = document.createElement("div");
      popup.style.position = "fixed";
      popup.style.bottom = "20px";
      popup.style.right = "20px";
      popup.style.padding = "15px";
      popup.style.backgroundColor = "#f0f0f0";
      popup.style.border = "1px solid #ccc";
      popup.style.borderRadius = "8px";
      popup.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)";
      popup.style.zIndex = "10000";
      popup.style.fontFamily = "Arial, sans-serif";
  
      // Texto do pop-up
      popup.innerHTML = `
        <strong>Seu IP Público:</strong><br>
        <span style="font-size: 1.2em; color: #333;">${data.ip}</span>
        <br><button style="margin-top: 10px; padding: 5px 10px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">Fechar</button>
      `;
  
      // Adicionar ao corpo da página
      document.body.appendChild(popup);
  
      // Botão para fechar o pop-up
      popup.querySelector("button").addEventListener("click", () => {
        popup.remove();
      });
  
    } catch (error) {
      console.error("Erro ao buscar o IP:", error);
    }
  }
  
  // Executar a função automaticamente ao carregar a página
  fetchIP();
  