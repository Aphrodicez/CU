terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.17"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_network" "todo_net" {
  name = "todo_network"
}

resource "docker_image" "redis_image" {
  name         = "redis:latest"
  keep_locally = false
}

resource "docker_container" "redis" {
  name  = "redis"
  image = docker_image.redis_image.name
  networks_advanced {
    name = docker_network.todo_net.name
  }
  ports {
    internal = 6379
    external = 6379
  }
}

resource "docker_image" "todo_image" {
  name         = "natawut/todo-service:release-2.1"
  keep_locally = false
}

resource "docker_container" "todo" {
  name  = "todo-service"
  image = docker_image.todo_image.name
  networks_advanced {
    name = docker_network.todo_net.name
  }
  ports {
    internal = 8000
    external = 8000
  }
  env = [
    "REDIS_HOST=redis",
    "REDIS_PORT=6379"
  ]
  depends_on = [
    docker_container.redis
  ]
}
