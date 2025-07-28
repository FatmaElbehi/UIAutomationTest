pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker and Docker Compose') {
            steps {
                script {
                    sh 'docker --version'
                    sh 'docker-compose up -d --build'
                    echo "Docker and Docker Compose OK"
                   
                }
            }
        }

        stage('Run Command Inside Docker Container') {
            steps {
                script {
                    sh 'docker exec -u root behave /bin/sh -c "behave -D browser=chrome"'

                    // step([
                    //     $class: 'DockerComposeBuilder', 
                    //     dockerComposeFile: 'docker-compose.yml', 
                    //     option: [
                    //         $class: 'ExecuteCommandInsideContainer', 
                    //         command: 'behave -D browser=chrome', 
                    //         index: 1, 
                    //         privilegedMode: true, 
                    //         service: 'behave', 
                    //         workDir: ''
                    //     ]
                    // ])
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                 sh 'docker exec -u root behave /bin/sh -c "allure generate allure-results --clean"'
            }
        }

stage('Deploy Report on Server') {
    steps {
        // Archive Allure report folder
        sh 'tar -czf allure-report.tar.gz allure-report'
        
        sshagent(['643018be-26f7-409b-8c9c-09e810a05216']) {
            // Connect to the server  test server
            sh("ssh -o StrictHostKeyChecking=no arvea_test@51.68.38.109  'ls -la'")
            sh 'rm -rf arvea_test@51.68.38.109:/var/www/vhosts/arvea-test.ovh/qa-report.arvea-test.ovh/allure-report'
            // Send archived file to the server using rsync (replace user, server, and path)
            sh 'rsync -avP  --delete allure-report.tar.gz arvea_test@51.68.38.109:/var/www/vhosts/arvea-test.ovh/qa-report.arvea-test.ovh/'
        }
        
        // Clean up local archive
        sh 'rm allure-report.tar.gz'
    }
}

        stage('Receive and Extract on Server') {
            steps {
                script {
                    sshagent(['643018be-26f7-409b-8c9c-09e810a05216']) {
                        // Extract the archived file on the server
                      sh 'ssh -o StrictHostKeyChecking=no arvea_test@51.68.38.109 "tar -xzf /var/www/vhosts/arvea-test.ovh/qa-report.arvea-test.ovh/allure-report.tar.gz -C /var/www/vhosts/arvea-test.ovh/qa-report.arvea-test.ovh/"'

                        // Clean up server-side archive
                      sh 'ssh arvea_test@51.68.38.109 "rm /var/www/vhosts/arvea-test.ovh/qa-report.arvea-test.ovh/allure-report.tar.gz"'
                    }
                }
            }
        }

        stage('Send Email Notification') {
            steps {
                script {
                    def emailList = ['mohamed.nacer.benkhlifa@maisonduweb.com', 'nourhen@maisonduweb.com', 'walaghais@gmail.com' ,'ines@maisonduweb.com']
                    def message = 'Allure report generated successfully .'
                    def allureReportUrl = 'https://qa-report.arvea-test.ovh/'
                    // Construct message with report link
                     message += '\n\n[View Allure Report](' + allureReportUrl + ')'
                    // Add steps to send email notification
                    emailext attachLog: true, body: message , subject: 'Allure Report', to: emailList.join(',')
                }
            }
        }

        stage('Send Discord Notification') {
            steps {
                script {
                 def webhookUrl = 'https://discord.com/api/webhooks/1104871766230319115/eBhGndDXoVP_pl1rBv4ZDmG_sPusYajTl2odjo3GMnU-HyUuE_srcnVvIK0x-KYMHuXO?thread_id=1203973244328345631'
                 def message = 'Allure report generated successfully .'
                 def allureReportUrl = 'https://qa-report.arvea-test.ovh/'
                 // Construct message with report link
                 message += '\n\n[View Allure Report](' + allureReportUrl + ')'
                // Construct JSON payload for Discord message
                def payload = [
                username: 'Jenkins',
                avatar_url: 'https://yourjenkins.com/logo.png', // URL to Jenkins logo
                content: message
                ]  

               // Convert payload to JSON string
               def jsonPayload = groovy.json.JsonOutput.toJson(payload)
            // Send HTTP POST request to Discord webhook URL
            sh "curl -X POST -H 'Content-Type: application/json' -d '${jsonPayload}' ${webhookUrl}"

                }
            }
        }
    }
}
