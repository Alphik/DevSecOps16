# prometheus and grafana and exporter 
 start with creating the node-exporter container

```bash
docker run --name node-exporter -p 9100:9100 -v /proc:/host/proc:ro -v /sys:/host/sys:ro -v /:/rootfs:ro prom/prometheus
```

and now you can access the metrics in http://localhost:9100/metrics

and now create the prometheus file:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: node-exporter
    static_configs:
      - targets: ["host.docker.internal:9100"] # in linux use contanername:9100
  - job_name: prometheus
    static_configs:
      - targets: ["localhost:9090"]
```

open terminal in the pwd of the file

and run

```bash
docker run --name=prometheus -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

and now you can see the prometheus webui in localhost:9090

and you can see the metrics and targets
