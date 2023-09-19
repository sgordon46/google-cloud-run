# Prisma Cloud Workload Protection 

[Workload protection](https://www.prismacloud.io/)

## App-embedded Defender with Google Cloud Run

In this repoistory, we are automatically deploying an application that is protected with an app-embedded defender.  We have also included steps doe deplying the associated cwp collection and cwp policy. 

[Google Cloud Run](https://cloud.google.com/run) is our Google service of choice for this deployment. 

The automation tool of choice is [Github Actions](https://github.com/actions)


## Requirements for Deployment
3 Secrets are needed for this project, and they should be configured in the **Actions secrets and variables** section of the repo

  - Prisma Cloud Compute API URL - PCC_API
  - Prisma Cloud Access Key - PCC_KEY
  - Prisma Cloud Secret Key - PCC_SET

Google Cloud Platform also provides keyless authentication and some of my notes are documented, but I followed the steps [here](https://github.com/google-github-actions/auth#setup) 

[Here is a link to my notes](authentication.md) - TODO (More to be flushed out here)



## Executing the application
- Once the Workflow script is executed and finishes without error.
- Navigate to the URL provided by the Google Cloud Run interface
  - Similar to https://<application name>-tc6llqn2zq-uc.a.run.app
  - TODO (Insert Image)
- At this link [HL7 Sample Messages](https://docs.webchartnow.com/functions/system-administration/interfaces/sample-hl7-messages/) you can find some sample HL7 message, and HL7 is the spec for how medical devices communicate. 
- Here is a sample from the site. 

```MSH|^~\&|SENDING_APPLICATION|SENDING_FACILITY|RECEIVING_APPLICATION|RECEIVING_FACILITY|20110613061611||SIU^S12|24916560|P|2.3||||||```

- Once the app is loaded, drop the above message into the Form field and choose submit. 
- This will properly submit the form and give a result back in json form. 
- To run the attack, modify the URL to replace the form data with something to the following.
  - ```ls -la```
  - ```cat /etc/shawdow```
  - ```whoami```
- You will now view in the output the output from these commands, which are harmless, but an attacker could take advantage of this opening and run commands that are more threatning. 
- Repeat the folowwing steps after enabling the **prevent** effect in the app-embedded policy in Prisma Cloud (TODO) Add photo