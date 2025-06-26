# Stage 1: Build the Go backend
FROM golang:1.21 as builder

WORKDIR /app

# Copy go.mod and go.sum
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the application
COPY . .

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux go build -o blog .

# Stage 2: Create minimal image
FROM alpine:latest

# Install timezone support and MariaDB client if needed
RUN apk add --no-cache ca-certificates tzdata mariadb-client

WORKDIR /app

# Copy compiled binary and templates
COPY --from=builder /app/blog .
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/static ./static

# Expose the port your Gin app runs on
EXPOSE 8080

# Run the server
CMD ["./blog"]

