// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "Canary",
    products: [
        .library(name: "Canary", targets: ["Canary"]),
    ],
    targets: [
        .target(name: "Canary"),
        .testTarget(name: "CanaryTests", dependencies: ["Canary"]),
    ]
)
