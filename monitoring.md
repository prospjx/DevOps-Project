# Monitoring

## Prometheus

Used to collect and store metrics and allows metrics to be queried using PromQL.

Metrics include: CPU usage, Memory usage, Pod status

## Grafana

Visualizes metrics collected from data sources for better understanding

## Monitoring Architecture

Kubernetes
    ↓
Metrics
    ↓
Prometheus
    ↓
Grafana
    ↓
Dashboards