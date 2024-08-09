          resources:
            requests:
              memory: "128Mi"
              cpu: "100m"
            limits:
              memory: "256Mi"
              cpu: "200m"


These were tested to be working, and they seem sensible. 
128 megabytes of RAM, and 100 millicores should be a good request for the project. The limits are good to be set higher than that.