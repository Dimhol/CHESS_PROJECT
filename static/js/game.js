document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('chessboard');
    const ctx = canvas.getContext('2d');
    const status = document.getElementById('status');
    const resetButton = document.getElementById('reset');
    const squareSize = 100;
    let selectedPiece = null;

    const board = [
        ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook'],
        ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'],
        ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
    ];

    const pieces = {
        'rook': '♜',
        'knight': '♞',
        'bishop': '♝',
        'queen': '♛',
        'king': '♚',
        'pawn': '♟︎'
    };

    const colors = ['#f0d9b5', '#b58863'];

    function drawBoard() {
        for (let row = 0; row < 8; row++) {
            for (let col = 0; col < 8; col++) {
                const color = colors[(row + col) % 2];
                ctx.fillStyle = color;
                ctx.fillRect(col * squareSize, row * squareSize, squareSize, squareSize);

                const piece = board[row][col];
                if (piece) {
                    ctx.fillStyle = 'black';
                    ctx.font = '80px Arial';
                    ctx.fillText(pieces[piece], col * squareSize + 10, row * squareSize + 75);
                }
            }
        }
    }

    canvas.addEventListener('click', function (event) {
        const col = Math.floor(event.offsetX / squareSize);
        const row = Math.floor(event.offsetY / squareSize);

        if (selectedPiece) {
            // Move piece logic
            const [fromRow, fromCol] = selectedPiece;
            board[row][col] = board[fromRow][fromCol];
            board[fromRow][fromCol] = '';
            selectedPiece = null;
            status.textContent = "Move made!";
        } else {
            if (board[row][col]) {
                selectedPiece = [row, col];
                status.textContent = `Selected ${board[row][col]}`;
            }
        }

        drawBoard();
    });

    resetButton.addEventListener('click', function () {
        // Reset game logic
        location.reload();
    });

    drawBoard();
});
