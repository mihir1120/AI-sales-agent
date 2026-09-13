import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Sales AI Agent",
  description: "V1 foundation for a sales AI agent.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
