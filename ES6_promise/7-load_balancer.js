export default function loadBalancer(chinaDownloead, USDownload) {
    return Promise.race([chinaDownloead, USDownload]);
}
