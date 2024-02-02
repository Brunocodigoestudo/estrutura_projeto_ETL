$port = 8000

# Verifica se há uma conexão na porta específica
$connection = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue

if ($connection -ne $null) {
    $processId = $connection.OwningProcess

    if ($processId -ne $null) {
        # Tenta encerrar o processo com privilégios elevados
        Start-Process powershell -Verb RunAs -ArgumentList "-File 'C:\caminho\para\seu\projeto\kill.ps1'"
        
        # A linha abaixo pode ser omitida, dependendo de como você deseja tratar a execução após solicitar privilégios
        Write-Host "Processo encerrado com sucesso na porta $port."
    }
    else {
        Write-Host "Erro: Não foi possível obter o ID do processo na porta $port."
    }
}
else {
    Write-Host "Nenhuma conexão encontrada na porta $port."
}


