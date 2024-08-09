          resources:
            requests:
              memory: "64Mi"
              cpu: "100m"
            limits:
              memory: "128Mi"
              cpu: "200m"



These were tested to be working, and they seem sensible for a light-weight webapp. 128 megabytes of RAM, and 100 millicores should be a good request for the project.