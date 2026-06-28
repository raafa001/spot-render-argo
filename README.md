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

### Tecnologias
- Argo Workflows + EventSource/Sensor  
- Blender headless  
- Python scripts (conversão/render)  
- Docker/ECR  
- GitHub Actions (lint + build/push)  
- Namespaces `rendering` (workflows) e `spot-render` (serviços).

### Métricas & Alertas
- Cada etapa pode publicar métricas via exporter (`render_success_total`, `render_error_total`, `render_duration_seconds`).  
- Para adicionar novas métricas, envie eventos HTTP para o exporter ou grave linhas no formato `METRIC=value` consumidas por `spot-render-observability`.  
- Alertas de canário são herdados do Rollout da API/Portal; para alertas específicos do workflow (ex.: falhas consecutivas), utilize `WorkflowEventBinding` e Prometheus rules.

### Testes locais
- Use `spot-render-teste-local` para instalar o Argo Workflows/Events no cluster local.  
- Execute `make build-worker` para gerar a imagem e `kind load docker-image` antes de aplicar `workflows/render.yaml`.  
- Configure variáveis `AWS_REGION`, `S3_*` via Secrets/ConfigMap localmente ou utilize MinIO conforme o README do repositório de teste.  
- Para validar sem Blender real, substitua o comando por `sleep` no YAML de desenvolvimento.

### TechDocs
- Documentação detalhada em `docs/index.md` + `mkdocs.yml` para publicação no Backstage.
