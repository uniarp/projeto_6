document.addEventListener('DOMContentLoaded', function() {
    // Função para abrir o modal
    function openModal() {
        document.getElementById('successModal').style.display = 'block';
    }

    // Função para fechar o modal
    function closeModal() {
        document.getElementById('successModal').style.display = 'none';
    }

    // Fechar o modal ao clicar no "X"
    document.querySelector('.close').addEventListener('click', closeModal);

    // Fechar o modal se o usuário clicar fora do conteúdo do modal
    window.onclick = function(event) {
        if (event.target == document.getElementById('successModal')) {
            closeModal();
        }
    }

    // Abrir o modal se a variável de sucesso estiver presente
    if (document.getElementById('showModal').value === 'True') {
        openModal();
    }
});

// Limpar os campos
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('successModal');
    const closeModal = document.querySelector('.close');
    const showModal = document.getElementById('showModal').value;
    const form = document.querySelector('form');

    if (showModal === 'True') {
        modal.style.display = 'block';
        // Limpar campos do formulário
        form.reset();
    }

    closeModal.onclick = () => {
        modal.style.display = 'none';
    };

    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
});
