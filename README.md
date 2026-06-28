## spot-render-argo

> **PT-BR:** Contém os Workflows do Argo, sensores S3, scripts Blender (conversão FBX → Principled + render headless) e Dockerfile do worker. Responsável por processar uploads e gerar saídas nos buckets output/error.

> **EN:** Hosts Argo Workflows, S3 sensors, Blender scripts (FBX → Principled + headless render) and the worker Dockerfile.

### Estrutura

```
workflows/render.yaml
sensors/s3-listener.yaml
scripts/convert_materials.py
scripts/render_blender.py
Dockerfile.worker

k8s/
  workflow-template.yaml
  configmap-scripts.yaml
```

### CI/CD

`.github/workflows/ci.yml` lint os manifests, constrói a imagem do worker (Blender) e publica no ECR.

### Observabilidade

Os scripts emitirão logs estruturados e sinais para o exporter Prometheus (spots registrados em `spot-render-observability`).
