# Fastapi-docker-template

## 執行步驟
### 建立.env 給docker-compose使用
```shell script
vim .env

# 舉例來說
DOMAIN=mb0520-demo.ml
EMAIL=meatball0520@gmail.com
TRAEFIK_USER=admin
TRAEFIK_PASSWORD_HASH=$2y$10$zi5n43jq9S63gBqSJwHTH.nCai2vB0SW/ABPGg2jSGmJBVRo0A.ni # admin
```

### 建立憑證資訊
```shell script
touch acme.json
chmod 600 acme.json
```

## 還未完成的事情
- [ ] 將traefik 改成auth

