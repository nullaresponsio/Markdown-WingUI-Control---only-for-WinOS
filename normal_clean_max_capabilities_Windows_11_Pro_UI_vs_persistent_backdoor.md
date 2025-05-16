![alt text](<Difference between “normal” Windows UI search and the custom dual-wildcard UI.png>)

// Difference between “normal” Windows UI search and the custom dual-wildcard UI
//
// ─ Normal File Explorer / File-open dialog ─
//   • Accepts only  *  (match many)  and  ?  (match one)  wildcards.:contentReference[oaicite:1]{index=1}
//
// ─ Custom dual-wildcard concept  (previous mock-up) ─
//   • Adds a mode switch that lets users enable bracket-set patterns like  [0-9]  or  [abc].
//   • Internally just forwards the query to PowerShell-style APIs, so no change
//     to Explorer’s indexing engine is required.
//
// Effect: advanced users get precise character-range matching without dropping
// to a CLI, while the default experience (shown in the image above) stays
// identical for everyone else.

// Can a persistent backdoor change what you see?
//
// Yes—if it runs with sufficient privileges.  Examples:
//
//   • User-mode rootkits inject DLLs into Explorer.exe and hook Win32 APIs
//     (FindFirstFileW, EnumWindows, UI-draw calls) to hide or alter items.:contentReference[oaicite:2]{index=2}
//
//   • Kernel-mode rootkits filter I/O at the file-system driver layer so
//     Explorer never even “sees” certain files or directories.:contentReference[oaicite:3]{index=3}
//
//   • Both styles can also patch common‐dialog classes (IFileDialog, OpenFileName)
//     so the same objects stay invisible across apps.
//
// Defenses revolve around Secure Boot, Driver Signing, Windows Defender’s
// kernel sensors, and integrity tools like Microsoft’s RootkitRevealer;
// if the attacker is already in the kernel, visual output cannot be trusted.