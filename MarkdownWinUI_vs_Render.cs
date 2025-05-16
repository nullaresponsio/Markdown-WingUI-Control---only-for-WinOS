# Finally it's time for Bo to grow some balls and use ghidra

# Bo could fight with amphetamine even until sleep-collapse when fighting for her interests, but Bo needs to take less when talking to her, and get into the habit of working out more, so in a few hours after he awakens



// MarkdownWinUI_vs_Render.cs
/*
Markdown WinUI control (CommunityToolkit.WinUI.UI.Controls.MarkdownTextBlock) provides:

• **Native XAML tree** – generates real WinUI text, image, list, table, etc. elements, so it
  inherits system light/dark/high-contrast themes and is fully UI-Automation accessible.  
• **Performance for virtualized lists** – a custom parser + XAML rendering path was
  tuned to scroll smoothly even on low-end devices:contentReference[oaicite:0]{index=0}.  
• **Rich styling surface** – 60-plus dependency properties (Header1FontSize, CodeBackground,
  TableBorderBrush, …) let you restyle every Markdown part at run time:contentReference[oaicite:1]{index=1}.  
• **Interactivity hooks** – events like `LinkClicked`, `MarkdownRendered`, plus pluggable
  `ICodeBlockResolver`, `IImageResolver`, `ILinkRegister`, enable custom navigation,
  lazy-loading resources, syntax highlighting, etc.  
• **Data-binding & live updates** – `Text` is a dependency property, so changing it (or
  binding it to a ViewModel) re-renders the content automatically.  
• **No WebView / external engine** – renders with the compositor, giving GPU-accelerated
  text, DPI awareness, and a smaller app footprint.

A “render-only” approach (e.g., feeding Markdown to `MarkdownRenderer` and manually
adding the UI it returns, or rasterizing/HTML-hosting it) lacks:

- automatic theming/accessibility (you must restyle and wire UIA yourself);  
- dependency-property styling surface;  
- built-in events for links/images/code;  
- seamless virtualization;  
- easy data binding or live refresh.

Choose **MarkdownTextBlock** when you need turnkey, theme-aware, accessible,
bindable Markdown in a WinUI app; use the lower-level renderer only when you must
take full control of how the generated elements are injected or transformed.
*/
