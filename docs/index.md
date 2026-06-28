# Spot Render Argo – TechDocs

## Fluxo
1. Sensor S3 detecta objeto em `spot-render-input`.  
2. WorkflowTemplate `render` executa steps `fetch_input`, `convert_materials`, `render_blender`, `record_metrics`.  
3. Resultados vão para `spot-render-output` e erros para `spot-render-error`.

## Estrutura
```
workflows/render.yaml
sensors/s3-listener.yaml
scripts/convert_materials.py
scripts/render_blender.py
Dockerfile.worker
```

## Tecnologias
- Argo Workflows / Events
- Blender 3.6 headless
- Python scripts
- AWS S3 / IRSA

## Métricas
- Scripts devem atualizar `render_success_total`, `render_error_total`, `render_duration_seconds` via exporter (HTTP POST).  
- Para novas métricas, adicione chamadas no script e atualize o exporter.

## Alertas
- Configure Workflow Prometheus metrics ou utilize regras do exporter (`spot-render-observability`).  
- Exemplos: falhas consecutivas > 3, duração média > 1h.

## Teste local
1. Siga o repositório `spot-render-teste-local` para instalar Argo (+ MinIO).  
2. Build worker: `docker build -t spot-render-worker:dev -f Dockerfile.worker .`  
3. `kind load docker-image spot-render-worker:dev`.  
4. `kubectl apply -f workflows/render.yaml` e `sensors/s3-listener.yaml`.  
5. Faça upload de teste (CLI/portal) e monitore `argo logs`.

## TechDocs
- Publicar via `mkdocs.yml` neste repositório.
