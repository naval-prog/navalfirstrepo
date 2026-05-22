function Badge({ label, color = "#2E75B6" }) {
  return (
    <span
      style={{
        backgroundColor: color,
        color: "white",
        padding: "4px 10px",
        borderRadius: "12px",
        marginRight: "8px",
      }}
    >
      {label}
    </span>
  );
}

export default Badge;